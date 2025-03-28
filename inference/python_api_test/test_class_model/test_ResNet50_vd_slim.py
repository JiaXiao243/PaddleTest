# -*- coding: utf-8 -*-
# encoding=utf-8 vi:ts=4:sw=4:expandtab:ft=python
"""
test ResNet50_vd_act_qat model
"""

import os
import sys
import logging
import tarfile
import six
import wget
import pytest
import numpy as np

# pylint: disable=wrong-import-position
sys.path.append("..")
from test_case import InferenceTest

# pylint: enable=wrong-import-position


def check_model_exist():
    """
    check model exist
    """
    resnet50_slim_url = "https://paddle-qa.bj.bcebos.com/PaddleSlim/ACT_models/ResNet50_vd_act_qat.tar"
    if not os.path.exists("./ResNet50_vd_act_qat/inference.pdmodel"):
        wget.download(resnet50_slim_url, out="./")
        tar = tarfile.open("ResNet50_vd_act_qat.tar")
        tar.extractall()
        tar.close()
    if not os.path.exists("./case_image_data"):
        wget.download("https://paddle-qa.bj.bcebos.com/inference_model/case_image_data.tgz", out="./")
        tar = tarfile.open("case_image_data.tgz")
        tar.extractall()
        tar.close()


def test_config():
    """
    test combined model config
    """
    check_model_exist()
    test_suite = InferenceTest()
    test_suite.load_config(
        model_file="./ResNet50_vd_act_qat/inference.pdmodel", params_file="./ResNet50_vd_act_qat/inference.pdiparams"
    )
    test_suite.config_test()


@pytest.mark.win
@pytest.mark.server
@pytest.mark.config_disablegpu_memory
def test_disable_gpu():
    """
    test no gpu resources occupied after disable gpu
    """
    check_model_exist()
    test_suite = InferenceTest()
    test_suite.load_config(
        model_file="./ResNet50_vd_act_qat/inference.pdmodel", params_file="./ResNet50_vd_act_qat/inference.pdiparams"
    )
    batch_size = 1
    fake_input = np.random.randn(batch_size, 3, 224, 224).astype("float32")
    input_data_dict = {"inputs": fake_input}
    test_suite.disable_gpu_test(input_data_dict)


@pytest.mark.win
@pytest.mark.server
@pytest.mark.slim
@pytest.mark.trt_int8
def test_trt_int8_more_bz():
    """
    compared trt_int8 batch_size=1 ResNet50_vd_act_qat outputs with true val
    """
    check_model_exist()

    file_path = "./case_image_data"
    images_size = 224
    batch_size_pool = [1]
    max_batch_size = 1
    for batch_size in batch_size_pool:
        test_suite = InferenceTest()
        if "win" in sys.platform:
            test_suite.load_config(
                model_file=".\\ResNet50_vd_act_qat\\inference.pdmodel",
                params_file=".\\ResNet50_vd_act_qat\\inference.pdiparams",
            )
        else:
            test_suite.load_config(
                model_file="./ResNet50_vd_act_qat/inference.pdmodel",
                params_file="./ResNet50_vd_act_qat/inference.pdiparams",
            )
        images_list, npy_list = test_suite.get_images_npy(file_path, images_size)
        fake_input = np.array(images_list[0:batch_size]).astype("float32")
        input_data_dict = {"inputs": fake_input}
        output_data_dict = test_suite.get_truth_val(input_data_dict, device="gpu")

        del test_suite

        test_suite = InferenceTest()
        test_suite.load_config(
            model_file="./ResNet50_vd_act_qat/inference.pdmodel",
            params_file="./ResNet50_vd_act_qat/inference.pdiparams",
        )
        test_suite.collect_shape_info(
            model_path="./ResNet50_vd_act_qat/", input_data_dict=input_data_dict, device="gpu"
        )
        del test_suite

        test_suite = InferenceTest()
        if "win" in sys.platform:
            test_suite.load_config(
                model_file=".\\ResNet50_vd_act_qat\\inference.pdmodel",
                params_file=".\\ResNet50_vd_act_qat\\inference.pdiparams",
            )
        else:
            test_suite.load_config(
                model_file="./ResNet50_vd_act_qat/inference.pdmodel",
                params_file="./ResNet50_vd_act_qat/inference.pdiparams",
            )
        test_suite.trt_bz1_slim_test(
            input_data_dict,
            output_data_dict,
            repeat=100,
            delta=1e-1,
            max_batch_size=max_batch_size,
            precision="trt_int8",
            min_subgraph_size=30,
            dynamic=True,
            shape_range_file="./ResNet50_vd_act_qat/shape_range.pbtxt",
            # use_calib_mode=True,
            with_benchmark=True,
            base_latency_ms=1.65,
            benchmark_threshold=5e-2,
        )

        del test_suite  # destroy class to save memory


@pytest.mark.win
@pytest.mark.server
@pytest.mark.slim
@pytest.mark.mkldnn_int8
def test_mkldnn_int8():
    """
    compared mkldnn_int8 batch_size=1 ResNet50_vd_act_qat outputs with true val
    """
    check_model_exist()

    file_path = "./case_image_data"
    images_size = 224
    batch_size = 1
    test_suite = InferenceTest()
    test_suite.load_config(
        model_file="./ResNet50_vd_act_qat/inference.pdmodel", params_file="./ResNet50_vd_act_qat/inference.pdiparams"
    )
    images_list, npy_list = test_suite.get_images_npy(file_path, images_size)
    fake_input = np.array(images_list[0:batch_size]).astype("float32")
    input_data_dict = {"inputs": fake_input}
    output_data_dict = test_suite.get_truth_val(input_data_dict, device="cpu")

    del test_suite  # destroy class to save memory

    test_suite2 = InferenceTest()
    test_suite2.load_config(
        model_file="./ResNet50_vd_act_qat/inference.pdmodel", params_file="./ResNet50_vd_act_qat/inference.pdiparams"
    )
    test_suite2.mkldnn_test(
        input_data_dict,
        output_data_dict,
        repeat=100,
        precision="int8",
        cpu_num_threads=10,
        with_benchmark=True,
        delta=2e-1,
        base_latency_ms=10.47,
        benchmark_threshold=5e-2,
    )

    del test_suite2  # destroy class to save memory

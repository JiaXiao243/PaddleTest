# api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.common.interpolate||method:__add__||api:paddle.nn.functional.common.interpolate||method:__add__||api:paddle.nn.functional.common.interpolate||method:__add__||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.pooling.max_pool2d
import paddle
import unittest
import numpy as np


class LayerCase(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
        self.parameter_0 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_1 = self.create_parameter(
           shape=[256, 256, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_2 = self.create_parameter(
           shape=[256, 512, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_3 = self.create_parameter(
           shape=[256, 2048, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_4 = self.create_parameter(
           shape=[256, 256, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_5 = self.create_parameter(
           shape=[256, 256, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_6 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_7 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_8 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_9 = self.create_parameter(
           shape=[256, 256, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_10 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_11 = self.create_parameter(
           shape=[256, 1024, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_12 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_13 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_14 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_15 = self.create_parameter(
           shape=[256, 256, 3, 3],
           dtype=paddle.float32,
        )
    def forward(
        self,
        var_0,    # (shape: [1, 256, 176, 176], dtype: paddle.float32, stop_gradient: True)
        var_1,    # (shape: [1, 512, 88, 88], dtype: paddle.float32, stop_gradient: False)
        var_2,    # (shape: [1, 1024, 44, 44], dtype: paddle.float32, stop_gradient: False)
        var_3,    # (shape: [1, 2048, 22, 22], dtype: paddle.float32, stop_gradient: False)
    ):
        var_4 = paddle.nn.functional.conv._conv_nd(var_0, self.parameter_1, bias=self.parameter_8, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_5 = paddle.nn.functional.conv._conv_nd(var_1, self.parameter_2, bias=self.parameter_12, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_6 = paddle.nn.functional.conv._conv_nd(var_2, self.parameter_11, bias=self.parameter_0, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_7 = paddle.nn.functional.conv._conv_nd(var_3, self.parameter_3, bias=self.parameter_14, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_8 = paddle.nn.functional.common.interpolate(var_7, scale_factor=2.0, mode='nearest')
        var_9 = var_6.__add__(var_8)
        var_10 = paddle.nn.functional.common.interpolate(var_9, scale_factor=2.0, mode='nearest')
        var_11 = var_5.__add__(var_10)
        var_12 = paddle.nn.functional.common.interpolate(var_11, scale_factor=2.0, mode='nearest')
        var_13 = var_4.__add__(var_12)
        var_14 = paddle.nn.functional.conv._conv_nd(var_13, self.parameter_15, bias=self.parameter_6, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_15 = paddle.nn.functional.conv._conv_nd(var_11, self.parameter_5, bias=self.parameter_7, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_16 = paddle.nn.functional.conv._conv_nd(var_9, self.parameter_9, bias=self.parameter_13, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_17 = paddle.nn.functional.conv._conv_nd(var_7, self.parameter_4, bias=self.parameter_10, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_18 = paddle.nn.functional.pooling.max_pool2d(var_17, 1, stride=2)
        return var_14, var_15, var_16, var_17, var_18


def create_paddle_inputs():
    inputs = (
        paddle.rand(shape=[1, 256, 176, 176], dtype=paddle.float32),
        paddle.rand(shape=[1, 512, 88, 88], dtype=paddle.float32),
        paddle.rand(shape=[1, 1024, 44, 44], dtype=paddle.float32),
        paddle.rand(shape=[1, 2048, 22, 22], dtype=paddle.float32),
    )
    return inputs


def create_numpy_inputs():
    inputs = (
        np.random.random(size=[1, 256, 176, 176]).astype('float32'),
        np.random.random(size=[1, 512, 88, 88]).astype('float32'),
        np.random.random(size=[1, 1024, 44, 44]).astype('float32'),
        np.random.random(size=[1, 2048, 22, 22]).astype('float32'),
    )
    return inputs


class TestLayer(unittest.TestCase):
    def setUp(self):
        self.inputs = create_paddle_inputs()
        self.net = LayerCase()
    def train(self, net, to_static, with_prim=False, with_cinn=False):
        if to_static:
            paddle.set_flags({'FLAGS_prim_all': with_prim})
            if with_cinn:
                build_strategy = paddle.static.BuildStrategy()
                build_strategy.build_cinn_pass = True
                net = paddle.jit.to_static(net, build_strategy=build_strategy, full_graph=True)
            else:
                net = paddle.jit.to_static(net, full_graph=True)
        paddle.seed(123)
        outs = net(*self.inputs)
        return outs
    def test_ast_prim_cinn(self):
        st_out = self.train(self.net, to_static=True)
        cinn_out = self.train(self.net, to_static=True, with_prim=True, with_cinn=True)
        for st, cinn in zip(paddle.utils.flatten(st_out), paddle.utils.flatten(cinn_out)):
            np.testing.assert_allclose(st.numpy(), cinn.numpy(), atol=1e-8)


if __name__ == '__main__':
    unittest.main()
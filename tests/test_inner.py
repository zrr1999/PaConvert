# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import textwrap

from apibase import APIBase

obj = APIBase("torch.inner")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.inner(torch.tensor([1., 2, 3]), torch.tensor([0., 2, 1]))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0.8173, 1.0874, 1.1784], [0.3279, 0.1234, 2.7894]])
        y = torch.tensor([[[-0.4682, -0.7159,  0.1506],
                        [ 0.4034, -0.3657,  1.0387],
                        [ 0.9892, -0.6684,  0.1774],
                        [ 0.9482,  1.3261,  0.3917]],
                        [[ 0.4537,  0.7493,  1.1724],
                        [ 0.2291,  0.5749, -0.2267],
                        [-0.7920,  0.3607, -0.3701],
                        [ 1.3666, -0.5850, -1.7242]]])
        result = torch.inner(x, y)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([[0.8173, 1.0874, 1.1784], [0.3279, 0.1234, 2.7894]])
        result = torch.inner(x, torch.tensor(2.))
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.inner(input=torch.tensor([1., 2, 3]), other=torch.tensor([0., 2, 1]))
        """
    )
    obj.run(pytorch_code, ["result"])


# The paddle input does not support integer type
def _test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.inner(torch.tensor([1, 2, 3]), torch.tensor([0, 2, 1]))
        """
    )
    obj.run(pytorch_code, ["result"])

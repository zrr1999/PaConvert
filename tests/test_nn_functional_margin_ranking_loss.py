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

obj = APIBase("torch.nn.functional.margin_ranking_loss")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input1 = torch.tensor([-1.0908,  0.1678,  0.6000,  0.0818])
        input2 = torch.tensor([ 1.0357,  0.4492, -0.3719, -0.4501])
        target = torch.tensor([-1., -1.,  1.,  1.])
        result = F.margin_ranking_loss(input1, input2, target)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input1 = torch.tensor([-1.0908,  0.1678,  0.6000,  0.0818])
        input2 = torch.tensor([ 1.0357,  0.4492, -0.3719, -0.4501])
        target = torch.tensor([-1., -1.,  1.,  1.])
        result = F.margin_ranking_loss(input1, input2, target, margin=0.8)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input1 = torch.tensor([-1.0908,  0.1678,  0.6000,  0.0818])
        input2 = torch.tensor([ 1.0357,  0.4492, -0.3719, -0.4501])
        target = torch.tensor([-1., -1.,  1.,  1.])
        result = F.margin_ranking_loss(input1, input2, target, margin=0.8, reduction='sum')
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input1 = torch.tensor([-1.0908,  0.1678,  0.6000,  0.0818])
        input2 = torch.tensor([ 1.0357,  0.4492, -0.3719, -0.4501])
        target = torch.tensor([-1., -1.,  1.,  1.])
        result = F.margin_ranking_loss(input1, input2, target, reduce=False, size_average=True)
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        import torch.nn.functional as F
        input1 = torch.tensor([-1.0908,  0.1678,  0.6000,  0.0818])
        input2 = torch.tensor([ 1.0357,  0.4492, -0.3719, -0.4501])
        target = torch.tensor([-1., -1.,  1.,  1.])
        result = F.margin_ranking_loss(input1, input2, target, reduce=False, size_average=False, reduction='mean')
        """
    )
    obj.run(pytorch_code, ["result"])

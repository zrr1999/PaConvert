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

obj = APIBase("torch.randint")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint(3, 5, (3,))
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint(10, (2, 2))
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_3():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint(3, 10, (2, 2), dtype=torch.int32, requires_grad=False)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_4():
    pytorch_code = textwrap.dedent(
        """
        import torch
        result = torch.randint(3, 10, (2, 2), dtype=torch.int32)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_5():
    pytorch_code = textwrap.dedent(
        """
        import torch
        out = torch.empty(2, 2, dtype=torch.int32)
        result = torch.randint(3, 10, (2, 2), out=out, dtype=torch.int32, layout=torch.strided, device=torch.device('cpu'), pin_memory=False, requires_grad=False)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)


def test_case_6():
    pytorch_code = textwrap.dedent(
        """
        import torch
        flag = False
        result = torch.randint(3, 10, (2, 2), dtype=torch.int64, requires_grad=flag)
        """
    )
    obj.run(pytorch_code, ["result"], check_value=False)

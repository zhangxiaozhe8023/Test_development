#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/7/27 20:56
# @Author : apple
# @Software: PyCharm
import pytest

@pytest.mark.parametrize("te_imput,expect,aa",
                        [
                            ([1,2,3]),
                            ([4,5,6]),
                            ([7,8,9])
                        ]
                        )

def test_demo(te_imput,expect,aa):
   print(te_imput,expect,aa)
   # print(str(te_imput[0]))
   print ( type ( te_imput ) )

   # aa={
   #     'ddd3':33,
   #     'dd':34,
   #     'd2':4
   # }
   # print(aa['ddd3'])

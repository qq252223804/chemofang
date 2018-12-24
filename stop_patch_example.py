#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
如果项目使用utx，在调试单个用例的时候，需要先调用utx.stop_patch()，暂停utx对unittest模块的注入
"""
import utx
utx.stop_patch()  # 如果注释掉这句，运行会报错

from Case.test2_dealer_SelfCar import Dingjia
import unittest

suite = unittest.TestSuite()
suite.addTest(Dingjia("test_upload_pictures"))
suite.addTest(Dingjia("test_change_headshot"))

unittest.TextTestRunner(verbosity=3).run(suite)

#!/usr/bin/python3.6
# coding=utf-8
# Author: Sitven

import os

# 获取项目绝对路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# log文件路径
log_path = os.path.join(project_path, "report", "logs")

# 异常截图路径
img_path = os.path.join(project_path, "report", "img")

# html测试报告路径
report_path = os.path.join(project_path, "report", "report")

# 测试用例文件路径
case_path = os.path.join(project_path, 'testCase')

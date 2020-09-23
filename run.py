#!/usr/bin/python3.6
# coding=utf-8
# Author: 文

from unittest import defaultTestLoader
from common.HTMLReport import HTMLTestRunner
from common.globalparam import report_path, case_path


discover = defaultTestLoader.discover(start_dir=case_path, pattern='test*.py', top_level_dir=None)
file_name = report_path + '/' + u'report.html'
fp = open(file_name, 'wb')


if __name__ == "__main__":
    runner = HTMLTestRunner(stream=fp, title=u'web自动化测试报告', description='测试结果&测试')
    runner.run(discover)
    fp.close()

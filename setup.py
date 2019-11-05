#!/usr/bin/env python
# -*- coding:utf-8 -*-

######################################
# File Name: setup.py
# Author: Gavin Wu
# Mail: 471456858@163.com
# Created Time: 2019-11-05 14:12
######################################

from setuptools import setup, find_packages

setup(
	name = 'pykubectl',
	version = '11.5',
	keywords = ('pip', 'kubernetes'),
	description = 'kubernetes python client 再次封装',
	license = 'MIT Licence',

	url = 'https://github.com/billgavin/pykubectl',
	author = 'Gavin Wu',
	author_email = '471456858@163.com',

	packages = find_packages(),
	include_package_data = True,
	platforms = 'any',
	install_requires = ['kubernetes', 'fire']
)

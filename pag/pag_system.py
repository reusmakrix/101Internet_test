#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# __________________________________________________________________________________________________
def start():
	reload(sys)
	sys.setdefaultencoding('utf8')
	sys.setrecursionlimit(10000)
	sys.stderr.write("\x1b[2J\x1b[H") # clear terminal
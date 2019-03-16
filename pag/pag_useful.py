#! /usr/bin/env python
# -*- coding: utf-8 -*-


# __________________________________________________________________________________________________
def part_digits(text, delimitter, part_num):
	text2 =text.split(delimitter)[part_num].replace(' ', '')
	dd_str = ''
	dd = ['1','2','3','4','5','6','7','8','9','0']
	for l in text2:
		for d in dd:
			if l==d:
				dd_str+=d
	return dd_str
# __________________________________________________________________________________________________
def remove_utf8(text):
	return text.encode('ascii', 'ignore').decode('ascii')
# __________________________________________________________________________________________________
def add_utf8(text):
	return text.encode('utf-8').decode('utf-8')
# __________________________________________________________________________________________________
def loop(vv, callback):
	for i, v in enumerate(vv):
		callback()
# __________________________________________________________________________________________________
def has(el, arr):
	for a in arr:
		if a == el:
			return True
	return False

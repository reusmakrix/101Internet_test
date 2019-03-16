
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 
import requests 
import time as t

# __________________________________________________________________________________________________
def get(url,ops=None, timeout=0):
	
	if timeout > 0:
		try:
			r = requests.get(url, timeout, headers=ops[1], proxies = ops[2])
			soup = BeautifulSoup(r.text, 'html.parser')
			r.close()
			return soup
		except requests.exceptions.ConnectionError:
			print 'Connection refused'
			
	else:
		if ops:
			try:
				r = requests.get(url, headers=ops[1], proxies = ops[2])
				soup = BeautifulSoup(r.text, 'html.parser')
				r.close()
				return soup

			except requests.exceptions.ConnectionError:
				print 'Connection refused'
		else:
			try:
				r = requests.get(url)
				soup = BeautifulSoup(r.text, 'html.parser')
				r.close()
				return soup
			except requests.exceptions.ConnectionError:
				print 'Connection refused'
# __________________________________________________________________________________________________
def ts(el, param):
	try:
		param = el.find(param).text
	except:
		param = None
	return param
# __________________________________________________________________________________________________
def params(el, selector):
	result = []
	try:
		objs = el.find_all(selector)
		for o in objs:
			result.append({'key':o['name'], 'val':o.text})
		return result
	except:
		return None
# __________________________________________________________________________________________________
def tss(el, param):
	result = []
	try:
		objs = el.find_all(param)
		for o in objs:
			result.append(o.text)
		return result
	except:
		return None
# __________________________________________________________________________________________________
def get_soup_from_source(source):
	soup = BeautifulSoup(source, 'html.parser')
	return soup
# __________________________________________________________________________________________________
def bsaid(soup, selector):
	items = soup.find_all(id= selector)
	return items
# __________________________________________________________________________________________________
def bsac(soup, selector):
	items = soup.find_all(class_= selector)
	return items
# __________________________________________________________________________________________________
def bsaid(url, selector):
	soup = get(url)
	items = find_all_by_id(soup,selector)
	return items
# __________________________________________________________________________________________________
def bsc(url, selector):
	soup = get(url)
	item = soup.find(class_= selector)
	return item
# __________________________________________________________________________________________________
def bsc_soup(soup, selector):
	item = soup.find(class_= selector)
	return item
# __________________________________________________________________________________________________
def bsid(url, selector):
	soup = get(url)
	item = soup.find(id= selector)
	return item
# __________________________________________________________________________________________________
def bssc(url, selector):
	r = requests.get(url)
	soup = bs(url)
	items = bsac(soup,selector)
	return items
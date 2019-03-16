#! /usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common import desired_capabilities
#---------------------------------------------
from bs4 import BeautifulSoup
# -------------------------------------------- 
import requests as r
# --------------------------------------------
import time as t
import pag_strings as pst
# import pag_passpay_buttons as b


_d= None

# __________________________________________________________________________________________________
def sx(locator, el=None):
	if not el:
		el= _d
	return el.find_element_by_xpath(locator)
# __________________________________________________________________________________________________
def ssx(locator, el=None):
	if not el:
		el= _d
	return el.find_elements_by_xpath(locator)
# __________________________________________________________________________________________________
def sxw(locator, time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.XPATH, locator))
	)
	return el
# __________________________________________________________________________________________________
def s(locator, el=None):
	if not el:
		el= _d
	return el.find_element_by_css_selector(locator)
# __________________________________________________________________________________________________
def ss(locator, el=None):
	if not el:
		el= _d
	return el.find_elements_by_css_selector(locator)
# __________________________________________________________________________________________________
def sw(locator, time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.CSS_SELECTOR, locator))
	)
	return el
 # __________________________________________________________________________________________________
def sc(locator, el = None):
	if not el:
		el= _d
	return el.find_element_by_class_name(locator)
# __________________________________________________________________________________________________
def ssc(locator, el = None):
	if not el:
		el= _d
	return el.find_elements_by_class_name(locator)
# __________________________________________________________________________________________________
def stn(locator, el=None):
	if not el:
		el= _d
	return el.find_element_by_tag_name(locator)
# __________________________________________________________________________________________________
def sstn(locator, el=None):
	if not el:
		el= _d
	return el.find_elements_by_tag_name(locator)
# __________________________________________________________________________________________________
def scw(locator, time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.CLASS_NAME, locator))
	)
	return el
# __________________________________________________________________________________________________
def satw(text,time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.LINK_TEXT, text))
	)
	return el
# __________________________________________________________________________________________________
def sid( locator, el=None):
	if not el:
		el= _d
	return	el.find_element_by_id(locator)
# __________________________________________________________________________________________________
def ssid(locator,el=None ):
	if not el:
		el= _d
	return	el.find_elements_by_id(locator)
# __________________________________________________________________________________________________	
def sidw(locator, time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.ID, locator))
	)
	return el
# __________________________________________________________________________________________________
def sn(locator, el=None):
	if not el:
		el= _d
	return	el.find_element_by_name(locator)
# __________________________________________________________________________________________________
def ssn(locator, el=None):
	if not el:
		el= _d
	return	el.find_elements_by_name(locator)
# __________________________________________________________________________________________________
def snw(locator,time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.NAME, locator))
	)
	return el
# __________________________________________________________________________________________________
def sat(text, el=None):
	if not el:
		el= _d
	return  el.find_element_by_link_text(text)
# __________________________________________________________________________________________________
def stn(locator, el=None):
	if not el:
		el= _d
	return el.find_element_by_tag_name(locator)
# __________________________________________________________________________________________________
def sstn(locator, el=None):
	if not el:
		el= _d
	return el.find_elements_by_tag_name(locator)
# __________________________________________________________________________________________________
def skel(el, keys):
	el.send_keys(keys)
# __________________________________________________________________________________________________
def ske(locator, keys):
	el = sn(locator)
	el.send_keys(keys)
	el.send_keys(Keys.ENTER)
# __________________________________________________________________________________________________
def skee(el, keys):
	el.send_keys(keys)
	el.send_keys(Keys.ENTER)
# __________________________________________________________________________________________________
def sk(locator, keys, el = None):
	if locator:
		sn(locator).send_keys(keys)
	else:
		if el:
			el.send_keys(keys)
# __________________________________________________________________________________________________
def slt(linktext, el=None):
	if not el:
		el= _d
	return el.find_element_by_link_text(linktext)
 # __________________________________________________________________________________________________
def sltw(locator, time):
	el = WebDriverWait(_d, time).until(
		EC.presence_of_element_located((By.LINK_TEXT, locator))
	)
	return el
# __________________________________________________________________________________________________
def splt(partlinktext, el=None):
	if not el:
		el= _d
	return el.find_element_by_partial_link_text(partlinktext)
# __________________________________________________________________________________________________
# def spltw(partlinktext, time):
# 	el = WebDriverWait(_d, time).until(
# 		EC.presence_of_element_located((By.NAME, partlinktext))
# 	)
# 	return el
# __________________________________________________________________________________________________
def par(el):

	return sx(el, "..")
# __________________________________________________________________________________________________
def js_script(script):
	return _d.execute_script(script)
# __________________________________________________________________________________________________
def js(code, el):

	return _d.execute_script('arguments[0].'+code, el)
# __________________________________________________________________________________________________
def js_scroll_to(el):
	code = 'scrollIntoView();'
	return js(code, el)
# __________________________________________________________________________________________________
def js_get_next(el):
	code = 'rnextElementSibling'
	return js(code, el)
# __________________________________________________________________________________________________
def a_move_to(el):
	hover = ActionChains(_d).move_to_element(el)
	hover.perform()
# __________________________________________________________________________________________________
def js_check_on(el):
	code = 'checked = true;'
	js(code, el)
# __________________________________________________________________________________________________
def js_check_off(el):
	code = 'checked = false;'
	js(code, el)
 # __________________________________________________________________________________________________
def js_click(el):
	code = 'click();'
	js(code, el)
# __________________________________________________________________________________________________
def js_get_option_text(select_el, option_num):
	code= 'options['+str(option_num)+'].text;'
	return js(code, select_el)
# __________________________________________________________________________________________________
def js_get_options_length(select_el):
	code = 'length;'
	# print 'JS: >>>>'+js(code, select_el)
	return js(code, select_el)
# __________________________________________________________________________________________________
def js_get_option_index(select_el):
	code = '''

	'''
	# print 'JS: >>>>'+js(code, select_el)
	return js(code, select_el)
# __________________________________________________________________________________________________
# def pp_select_man(option_txt, cb=None):
# 	sel = Select(b.links_tab_manufacturer_select())
# 	try:
# 		sel.select_by_visible_text(option_txt)
# 	except: #selenium.common.exceptions.NoSuchElementException:
# 		if cb:
# 			cb()
# __________________________________________________________________________________________________
# def pp_select_cat(option_txt, cb=None):
# 	sel = Select(b.links_tab_category_select())
# 	try:
# 		sel.select_by_visible_text(option_txt)
# 	except: #selenium.common.exceptions.NoSuchElementException:
# 		if cb:
# 			cb()
# __________________________________________________________________________________________________
def js_select(select_el, option_txt, cb=None):
	sel = Select(select_el)
	try:
		sel.select_by_visible_text(option_txt)
		return True
	except: #selenium.common.exceptions.NoSuchElementException:
		if cb:
			cb()
		else:
			return False
	# select_fr.select_by_index(js_get_option_index)
	# print '>>>    select_el : '+ select_el.

	# options_num =js_get_options_length(select_el)
	# print '>>>    options num : '+options_num
	# for i in range(options_num):
	# 	o_text = js_get_option_text(select_el, i)
	# 	if o_text == option_txt:
	# 		code = 'options['+str(i)+'].selected = true;'
	# 		js(code, select_el)
			# js_script(code)
# __________________________________________________________________________________________________
def js_scroll(el_id):
	script = '''
		$("#button").click(function() {
		$([document.documentElement, document.body]).animate({
		scrollTop: $("#%s").offset().top
		}, 2000);
});
	''' % el_id
	js_script(script)
# __________________________________________________________________________________________________
def js_skid(el_id, text):

	script = "document.getElementById('%s').value= '%s'%s" %(el_id, text, ';')
	script = pst.rwwr(script)
	# print '>>>    script : '+script
	js_script(script)
# __________________________________________________________________________________________________
def js_sktn(el_class, text):

	script = "document.getElementByTagName('%s')[0].value= '%s'%s" %(el_class, text, ';')
	script = pst.rwwr(script)
	# print '>>>    script : '+script
	js_script(script)
# __________________________________________________________________________________________________
def get_url():
	url = _d.current_url
	return url
# __________________________________________________________________________________________________
def get_source():
	source = _d.page_source
	return source
# __________________________________________________________________________________________________
def get_title():
	return _d.title
# __________________________________________________________________________________________________
def log():
	try:
		return _d.get_log('browser')[-1]['message']
	except IndexError:
		return 'no logs yet'
# __________________________________________________________________________________________________
def st(text):
	source = get_source()
	if text in source:
		return True
	else:
		return False
# __________________________________________________________________________________________________
# def goTo( url ):
#     if "errorPageContainer" in [ elem.get_attribute("id") for elem in s("body > div") ]:
#         raise Exception( "this page is an error" )
#     else:
#         _d.get( url )
# __________________________________________________________________________________________________
def get_scrolled_source(url=None, options=None):
	# Selenium script to scroll to the bottom, 
	# wait 6 seconds for the next batch of data to load, 
	# then continue scrolling.
	# It will continue to do this until the page stops loading new data.
	if url:
		start_driver(20, url,[options[0], options[1], options[2]])
		print u'заголовок страницы :'+ get_title()
	script = """
	window.scrollTo(0, document.body.scrollHeight);
	var lenOfPage=document.body.scrollHeight;
	return lenOfPage;
	"""

	lenOfPage = js_script(script)
	match=False
	while(match==False):
		lastCount = lenOfPage
		t.sleep(6)
		lenOfPage = js_script(script)
		if lastCount==lenOfPage:
			match=True

			return get_source()
# __________________________________________________________________________________________________
def add_options(ops):
	options = Options()
	if ops[0]:
		options.add_argument("--headless") # запускает _d в режиме 'headless'
	if ops[1]:
		options.add_argument('--proxy-server=%s' % ops[1])
	if ops[2]:
		options.add_argument('--user-agent=%s' % ops[2]) 
	options.add_argument('--ignore-certificate-errors')
	options.add_argument('--start-maximized')

	return options
# __________________________________________________________________________________________________
def accept_alert():
	# _d.get("http://sandbox.dev/alert.html")
	alert = _d.switch_to_alert()
	alert.accept()
# __________________________________________________________________________________________________
def get_driver(ops):
	global _d
	if not _d:
		if ops:
			_d = webdriver.Chrome('drivers/chromedriver', chrome_options = add_options(ops))
	return _d
# __________________________________________________________________________________________________
def start_driver(timeout, url, ops):

	# PROXY = '23.23.23.23:3128' # IP:PORT or HOST:PORT	
	# global _d
	# if not _d:
	# 	_d = webdriver.Chrome('drivers/chromedriver', chrome_options = add_options(headless, proxy, agent))
	get_driver(ops)
	_d.set_window_position(0, 0)
	# _d.set_window_size(1024, 768)
	_d.set_window_size(1024, 600)
	_d.maximize_window()
	if url:
		if timeout:
			_d.implicitly_wait(timeout)
		_d.get( url )
	# else:
	# 	if url:
	# 		if timeout:
	# 			_d.implicitly_wait(timeout)
	# 		_d.get( url )
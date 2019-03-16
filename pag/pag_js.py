#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pag_selenium as sl
import time as t

# __________________________________________________________________________________________________
def select_attr(attr_name):
	script = '''
		var menu = document.getElementById('%s');
		options = menu.getElemementsByTagName('li')
		for (var i = 0; i < options.length; i++) {
		alert(options[i].innerHTML)
		if options[i].innerHTML === %s{
			options[i].click();
		}
	''' % ('dropdown-menu', attr_name)
	sl.js_script(script)
# __________________________________________________________________________________________________
def select(select_id, option_text):
	script ='''
			var sel = document.getElementById('%s');

			for (var i = 0; i < sel.options.length; i++) {
			opt = sel.options[i];
			if (opt.text === '%s') {
			alert(opt.text);
			//opt.selected =true
			sel.selectedIndex = i;
			break;
	    }
	}
	''' % (select_id, option_text)

	sl.js_script(script)
	# t.sleep(2)
	# sl.accept_alert()
	
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

_letters_ru = [
		u'а',
		u'б',
		u'в',
		u'г',
		u'д',
		u'ж',
		u'з',
		u'и',
		u'й',
		u'к',
		u'л',
		u'м',
		u'н',
		u'о',
		u'п',
		u'р',
		u'с',
		u'т',
		u'у',
		u'ф',
		u'х',
		u'ц',
		u'ш',
		u'щ',
		u'ъ',
		u'ь',
		u'э',
		u'ю',
		u'я'
	]
# __________________________________________________________________________________________________
def mf(text):# make_text_flat
	t1 = text.replace(',', ' ')
	t2=t1.replace('-',' ')
	t3 = t2.lower()
	t4 = t3.replace(' ', '')
	return rwwr(t4)
# __________________________________________________________________________________________________
def sarr(text, text_arr):
	for line in text_arr:
		if text in line:
			return line
	return None
# __________________________________________________________________________________________________
def ruv(word, text_arr, divider='-'):#return line value by word in line
	# try:
		return strip_ru(sarr(word, text_arr).split(divider)[1])
	# except IndexError:
	# 	return ''
# __________________________________________________________________________________________________
def gn(text):
	result=''
	dd = ['.','1','2','3','4','5','6','7','8','9','0']
	for l in text:
		for d in dd:
			if l== d:
				result+=l
	return result
# __________________________________________________________________________________________________
# def gn(text):
# 	result = ''
# 	# find all characters in the string that are numeric.
# 	m = re.search(r'\d+', text)
# 	if m:
# 		result += m # retrieve numeric string
# 		return result # returns 100
# __________________________________________________________________________________________________
def sw(str1, str2):
	if str1 in str2:
		return True
	return False
# __________________________________________________________________________________________________
def rwr(text):
	return re.sub(r'\s+', '', text)
# __________________________________________________________________________________________________
def rwwr(text):
	few_words = ''
	words = text.split(' ')
	# print '>>>    rwwr : '+text
	# print '>>>    rwwr : '+str(len(words))
	if len(words)>1:
		for word in words:
			if len(word)>0:
				word = re.sub(r'\s+', '', word)
				few_words+=word+' '
		return few_words
	else:
		return re.sub(r'\s+', '', text)
# __________________________________________________________________________________________________
# def rws(text): # remove whitespaces and line markers
# 	result = ''
# 	for l in text:
# 		if not l==' ' or not l==' \n' or not l=='\r ' :
# 			result.join(l)
# 		else:
# 			continue
# 	return result
# __________________________________________________________________________________________________
def rw(text):
	few_words = ''
	words = text.split(' ')
	if len(words)>1:
		for word in words:
			word=word.replace(' ','')
			few_words+=word+' '
		return few_words
	else:
		return text.replace(' ','')

	# result = ''
	# words = text.split(' ')
	# if len(words)>1:
	# 	for i, word in enumerate(words):
	# 		if i>0:
	# 			s = ' '
	# 		else:
	# 			s='' 
	# 		result+= s+word
	# 		# print 'rw:'+result
	# 		return result
	# else:
	# return text.replace(' ','')
# __________________________________________________________________________________________________
def strip_ru(text):
	strip = ''
	
	for l in text.decode('utf-8'):
		for k in _letters_ru:
			# ifl.decode('utf-8').lower()== k:
			if l.decode('utf-8').lower()== k:
				strip.join(l)
	return strip
# __________________________________________________________________________________________________
def gln(text, text_arr, line_num=None):# get text line num
	count = 0
	for i,line in enumerate(text_arr):
		if text in line:
			count+=1
			if line_num: 
				if count == line_num:
					return i
			else:
				return i

# __________________________________________________________________________________________________
def get_num(str_num):
	result = ''
	dd = ['0','1','2','3','4','5','6','7','8','9']
	for i,l in enumerate(str_num):
		for d in dd:
			if l == d:
				result+=d
			# elif d=='.' and i == len(str_num)+1:
				# continue
			else:
				continue
	# print 'st:float:'+result.split('.')[0]
	return result
# __________________________________________________________________________________________________
def get_float(str_num):
	result = ''
	dd = ['.','0','1','2','3','4','5','6','7','8','9']
	for i,l in enumerate(str_num):
		for d in dd:
			if l == d:
				result+=d
			# elif d=='.' and i == len(str_num)+1:
				# continue
			else:
				continue
	# print 'st:float:'+result.split('.')[0]
	return result	
# __________________________________________________________________________________________________
def get_round(str_num):
	str_num1 = get_float(str_num)
	str_int_part = get_num(str_num1.split('.')[0])
	str_round = str(int(str_int_part)+1)
	# print 'st: round:'+str_round
	return ''.join(str_round)
	# text2 = gn(rw(text))
	# # print 'price:'+ str(float(text2))
	# try:
 #   		return str(int(text2))
	# except ValueError:
	#    pass 
# __________________________________________________________________________________________________
def utf8(text):

	return text.encode('utf-8')
 #! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests 
import shutil
import os
from os import listdir


# __________________________________________________________________________________________________
def isfile(path):
	if os.path.isfile(path):
		return True
	return False
# __________________________________________________________________________________________________
def sif( img_url, img_file_path):
	# if not os.path.isfile(file_path):
	print '>>>    fl: saving img ...'
	# if not path(img_file_path):
		# variant 1(same effect)

		# with open('picture.png', 'rb') as f:
		# 	data = f.read()
		# with open('picture_out.png', 'wb') as f:
		# 	f.write(data)

		# variant 2(used)
	r = requests.get(img_url,stream=True)
	# try:
	with open(img_file_path,'wb') as f: 
		shutil.copyfileobj(r.raw, f)
	# except IOError:
	# 	print '    >>>    fl: Some Problems To Save Image Here...Return'
	# 	return # save img as file
# else:
# 	print '>>>    fl: image already exist. Return'
# 	return
# __________________________________________________________________________________________________
# def pipi(path):#pth inside inside path
# 	dirs = pi(path)
# 	for d in dirs:
# 		# file_path = path+d+'/'
# 		files = fl.rdarr(d)
# 	return files
# __________________________________________________________________________________________________
def pipi(dir_path):# get file paths inside dirs inside dir
	paths_inside_inside = []
	dirs1 = pi(dir_path)
	for d in dirs1:
		files = pi(d)
		for f in files:	
			paths_inside_inside.append(f)
	return paths_inside_inside
# __________________________________________________________________________________________________
def pi(dir_path):#get paths inside dir
	paths_inside = []
	items = rdarr(dir_path)
	for item in items:
		# print '>>>    fl: file : '+item
		item_path = dir_path+'/'+item
		paths_inside.append(item_path)
	return paths_inside
# __________________________________________________________________________________________________
def dmr(src, dst, dir_names):# move and rename dir
	for i, d in enumerate(dir_names):
		path(dst+str(d))
		src_dirs =rdarr(src)
		for src_d in src_dirs:
			print'>>>    src : '+src+src_d
			print'>>>    dest : '+dst+str(d)
			os.rename(src+src_d, dst+str(d))
		i+=1
# __________________________________________________________________________________________________
def f_move(src, dst):# move dir
	files = os.listdir(src)
	files.sort()
	for f in files:
	    f_src = src+f
	    f_dst = dst+f
	    shutil.move(f_src, f_dst) 
# __________________________________________________________________________________________________
def f_copy(src, dst): # copy dir
	files = os.listdir(src)
	files.sort()
	for f in files:
	    f_src = src+f
	    f_dst = dst+f
	    shutil.copy(f_src, f_dst)
	# path(new_dir_path)
	# shutil.move(src,dest)
	# try:
	# 	os.rename(old_dir_path, new_dir_path)
	# 	return True
	# except OSError:
	# 	print str(new_dir_path) +' : allready exist'
	# 	return False
	# files_from = rdarr()
	# for file_from in files_from:
	# 	dir_to =  
# __________________________________________________________________________________________________
def rdarr(dir_to_fill_from): # read dir data as arr
	arr = []
	# print '>>>    fl rdarr :' + dir_to_fill_from
	d = listdir(dir_to_fill_from.decode('utf-8'))
	# print d
	for f in d:
		# arr.append(f[0:-3].decode('utf-8'))
		arr.append(f.decode('utf-8'))
	return arr 
# __________________________________________________________________________________________________
def rfarr(file_path): # read file data as arr
	# print '>>>    fl rfarr :' + file_path
	try:
		f = open(file_path, 'r')
		arr = f.readlines()
		f.close()
		return arr
	except:
		print '>>>>>>>>>> rfarr:  file does not exist... Return'
		return #None
# __________________________________________________________________________________________________
def path(dir_path):  # check and create path
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
		return False
	else:
		return True
# __________________________________________________________________________________________________
def file_exist(file_path): # check file exist
	try:
		file_data = rfarr(file_path)
		if file_data:
			for line in file_data:
				if line =='done':
					return True
		else:
			return False
		return False 
	except:
		print '>>> fl.file_exist : file do not exist yet. Return'
		return
# __________________________________________________________________________________________________
def wtfar(file_path, text_array, mode='w', delimitter=''): # write to file data arr
	# if not file_exist(file_path):
		try:
			with open(file_path, mode) as f:
				for text_line in text_array:
					f.write("%s\n" % text_line.decode('utf-8'))
				f.close()
		except IOError:
				print '>>>   fl: Save Error..Return'
				return
# __________________________________________________________________________________________________
# def wtdar(dir_path, files_names_array, mode='w'):
# 	# if not file_exist(file_path):
# 		try:
# 			with open(dir_path, mode) as f:
# 				for file_name in files_names_array:
# 					f.write("%s\n" % text_line.decode('utf-8'))
# 				f.close()
# 		except IOError:
# 				print '>>>   fl: Save Error..Return'
# 				return
# __________________________________________________________________________________________________
def cbt(file_path, text, print_line=False): # count by text
	count = 0
	lines = rfarr(file_path)
	
	for i, line in enumerate(lines):
		if text in line:
			if print_line:
				print line
		count+=1
	print u'Всего найдено : '+str(count)
	return count
# __________________________________________________________________________________________________
def cbm(file_path, marker, line_offset=0, print_line=False): # count by marker offset text
	count = 0
	lines = rfarr(file_path)
	
	for i, line in enumerate(lines):
			if marker in line:
				if print_line:
					print u'>>> товар : '+lines[i+line_offset]#+' | '+ lines[i-2]
				count+=1
	print u'Всего найдено : '+str(count)
	return count
# __________________________________________________________________________________________________
def wd(data_txt):#write data to file
	for i, line in enumerate(lines):
		if text in line:
			if data_txt in line:
				print line
		count+=1
# __________________________________________________________________________________________________
def wtf(file_path, txt, mode='w', delimitter=''):# write text to file
	# if not file_exist(file_path):
		# if not path(file_path):
		# if not os.path.exists(file_path):
			# print 'fl: saving...'
		# if not os.path.isfile(file_path):
		try:
			with open(file_path, mode) as f:
				f.write(txt.decode('utf-8'))#+ delimitter)
				f.close()
		except IOError:
				print '>>>   fl: Save Error..Return'
				return
	# else:
	# 	print '>>>>>>>>>>    fl: File exist..Return'
	# 	return
#! /usr/bin/env python
# -*- coding: utf-8 -*
import xlrd
import csv

_header = None
# __________________________________________________________________________________________________
def get_header(o):
	first_line = []
	for key, value in o.iteritems():
		if key =='params':
			k=1
			for param in value:
				# if k<31:
				n = 'Attrubute %s name' %k
				v = 'Attrubute %s value' %k
				first_line.append(n.replace('"', ''))
				first_line.append(v.replace('"', ''))
				k+=1
		else:
			first_line.append(key.replace('"', ''))
	return first_line
# __________________________________________________________________________________________________
def wcr(o, csv_file_path):#write row to csv file for woocomerce
	global _header
	csv_file = open(csv_file_path.decode('utf-8'), 'a')
	# wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
	wr = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	
	if not _header:
		_header = get_header(o)
		wr.writerow(_header)

	csv_row =[]	
	for key, value in o.iteritems():
		# print key
		if key == 'Images':
			# for pic in value:
				# if(len(pic)>=6):
			# img_name = value.split('/')[-1]
			# img = 'https://kaminnaya1.ru/wp-content/uploads/2019/03/'+img_name
			csv_row.append(value)
		# elif key == 'params':
		# 	for param in value:
		# 		csv_row.append(param['name'])
		# 		csv_row.append(param['val'])			
		elif not value:
			csv_row.append(','.replace('"', ''))
		else:
			if not'.jpg'in value:
				csv_row.append(value)
	wr.writerow(csv_row)
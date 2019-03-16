#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pag import pag_selenium as sl
from pag import pag_bs as bs
from pag import pag_strings as st
from pag import pag_system as s
import datetime

_headless = True
months = [
	[1,"January"],
	[2,"Febuary"],
	[3,"March"],
	[4,"April"],
	[5, "May"],
	[6,"June"],
	[7,"July"],
	[8,"August"],
	[9,"September"],
	[10,"October"],
	[11,"November"],
	[12,"December"]
]
#______________________________________________________________________________________
def get_mon_num(mon):
	for month in months:
		if month[1] == mon:
			# print 'converted mon is:'+mon
			return month[0] 
#______________________________________________________________________________________
def item_date_earler(item_date, today_date):
	print'-------------------------------------'
	# print 'item date year:'+ str(item_date['year'])
	# print 'item date mon:'+get_mon_num(item_date['mon'])
	# print 'item date day:'+str(item_date['day'])

	# print 'today date year:'+ str(today_date['year'])
	# print 'today date mon:'+get_mon_num(today_date['mon'])
	# print 'today date day:'+str(today_date['day'])
	year_check = (int(item_date['year'])<int(today_date['year']))
	mounth_check = (get_mon_num(item_date['mon'])<get_mon_num(today_date['mon']))
	day_check = (int(item_date['day'])<int(today_date['day']))
	if year_check:
		return True
	elif year_check and mounth_check:
		return True
	elif year_check and mounth_check and day_check:
		return True
	return False
#______________________________________________________________________________________
def asin_in_text(tag):

	return tag.name == 'li' and 'ASIN' in tag.text

def data_in_text(tag):
	
	return tag.name == 'li' and 'Date first available at Amazon.com.au' in tag.text
#_______________________________________________________________________________________
def main():
	s.start()
	url = 'http://amazon.com.au'

	sl.start_driver(0,url,[_headless,None,None])
	print '>>>    got amazon page'
	categories_select = sl.sx('//*[@id="searchDropdownBox"]')
	category_found = sl.js_select(categories_select,'Pet Supplies')
	if category_found:
		print '>>>    pet supplies category selected'
		search_btn = sl.sx('//*[@id="nav-search"]/form/div[2]/div/input').click()
		cats_subcat = sl.sx('//*[@id="nav-subnav"]/a[4]/span')
		cats_subcat.click()
		print '>>>    cat clothing subcategory opened'
		next_page_btn = sl.sx('//*[@id="a-autoid-1"]/span/i')
		next_page_btn.click()

		cats_clothing_btn = sl.sx('//*[@id="anonCarousel2"]/ol/li[2]/div/a/div[1]/div/img')
		cats_clothing_btn.click()
		first_item = sl.sx('//*[@id="anonCarousel1"]/ol/li[1]/a/img')
		first_item.click()
		soup = bs.get_soup_from_source(sl.get_source())
		item_name_box = soup.find('span', id='productTitle')
		if item_name_box:
			item_name = item_name_box.text
			if len(item_name)>0:
				print '>>>    item title found'
				title_assert = True
			else:
				title_assert = False

		content = soup.find('div', class_='content')
		# content.find(lambda tag:tag.name=="li" and "ASIN" in tag.text)
		asin_box = content.find(asin_in_text)
		if asin_box:
			item_asin = asin_box.text
			if len(item_asin)>0:
				asin_assert = True
				print '>>>    item ASIN found'
			else:
				asin_assert = False

		else:
			item_asin = 'n/a'
		item_first_shown_time = st.rwwr(content.find(data_in_text).text.split(':')[1])

		date_today = datetime.datetime.now()
		today_day = str(date_today.day) 
		today_mon = date_today.strftime("%B")
		today_year =str(date_today.year )

		# print 'date today:'+ today_day+' '+today_mon+' '+today_year

		print 'item date:'+item_first_shown_time #28 September 2017
		item_date_parts=item_first_shown_time.split(' ')
		item_day=item_date_parts[0]
		item_mon=item_date_parts[1]
		item_year=item_date_parts[2]

		item_date = {'day':item_day,'mon':item_mon,'year': item_year}
		today_date = {'day':today_day,'mon':today_mon,'year': today_year}
		date_assert = item_date_earler(item_date, today_date)
		# date_result = datetime.now() - item_first_shown_time
		# if date_result>0:
		# 	date_assert = True
		# else:
		# 	date_assert = False

		print st.rwwr(item_name), st.rwwr(item_asin)
		print '-------------------------------------'
		print 'item Title exist:'+str(title_assert)
		print 'item ASIN exist:'+str(asin_assert)
		print 'Apears on Amazon earler than today :'+str(date_assert)



if __name__ == '__main__':
	main()
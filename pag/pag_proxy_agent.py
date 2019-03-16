#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


proxies =[
    '95.5.134.198:8080',
    '91.206.19.193:8081',
    '178.46.157.208:8080',
    '95.215.100.159:8888',
    '95.143.220.230:8888',
    '95.105.15.91:8080',
    '94.242.57.136:1448',
    '79.104.219.125:3128',
    '82.198.187.135:8081',
    '46.29.195.210:8080',
    '91.144.147.46:8080',
    '193.242.178.90:8080',
    '217.10.45.103:808',
    '31.28.0.204:8080',
    '89.207.93.228:8080',
    '94.242.58.142:1448',
    '46.73.33.253:8080',
    '91.235.247.252:808',
    '92.255.69.18:8080 ',
    '95.79.99.148:3128',
    '37.235.65.76:8080',
    '79.137.181.170:8080',
    '94.242.55.108:10010',
    '176.117.233.184:8080',
    '188.93.246.34:80',
    '185.22.172.94:10010',
    '31.211.83.67:8080',
    '109.173.73.116:80',
    '92.50.155.218:8080',
    '31.211.47.120:8080',
    '185.22.172.94:1448',
    '194.67.202.150:3128',
    '178.162.102.173:8081',
    '85.113.48.148:8080',
    '78.85.36.203:8080',
    '95.128.142.106:8080',
    '84.52.74.194:8080',
    '83.171.122.21:8080',
    '62.213.118.162:8080',
    '82.151.208.20:8080',
    '91.235.187.85:8080',
    '94.242.59.135:1448',
    '94.242.58.14:1448',
    '94.141.105.146:8080',
    '94.242.55.108:1448',
    '95.31.3.7:8085',
    '195.9.237.66:8080',
    '77.238.234.149:8081',
    '77.236.231.8:8088',
    '195.122.236.246:8080',
    '188.168.69.186:8080',
    '193.254.225.93:4550',
    '94.79.54.25:3128',
    '81.23.177.245:80 ',
    '109.194.50.73:808',
    '77.238.234.145:8081',
    '94.242.59.245:1448',
    '78.107.71.162:80 ',
    '89.148.195.140:8080',
    '62.140.252.21:8081',
    '95.80.98.41:8080 ',
    '88.84.223.56:3128 ',
    '185.130.104.163:8080',
    '94.242.59.245:10010',
    '5.16.15.234:8080',
    '77.95.94.213:8080',
    '95.78.177.232:8080',
    '185.42.164.29:8080',
    '109.173.73.116:8080',
    '94.242.59.135:10010',
    '37.228.89.215:80',
    '80.254.125.236:80',
    '92.51.36.1:8080',
    '80.245.117.131:8080',
    '94.141.190.130:8080',
    '92.124.195.22:3128',
    '85.143.66.78:8080',
    '5.16.15.2:8080',
    '188.35.31.254:58111',
    '83.171.102.39:8080',
    '195.122.236.246:8080',
    '94.242.59.135:10010'

]

agents=[
    'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    'Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)'
]
# __________________________________________________________________________________________________
# def get_proxy():
#     return {'http': 'http://'+ random.choise(proxies) }
# # __________________________________________________________________________________________________
# def get_agent():
#     return { 'User-Agent ':random.choise(agents) }
# __________________________________________________________________________________________________
def get_proxy():
    return ['http', ('http://'+ proxies[randint(0, len(proxies)-1)]) ]
# __________________________________________________________________________________________________
def get_agent():
    return ['User-Agent ', (agents[randint(0, len(agents)-1)]) ]
# __________________________________________________________________________________________________
def get_options(headless=False, need_proxy=True, need_agent=True):
    options = []
    if headless:
        options.append(True)
    else:
        options.append(False)

    if need_proxy:
        parts = get_proxy()
        proxy = [parts[0], parts[1]]
    else:
        proxy = ['http' , None]

    if need_agent:
        parts = get_agent()
        agent = [parts[0], parts[1]]
    else:
        agent = ['User-Agent ', None]
    i= '\''
    c = ':'
    options.append({proxy[0] : proxy[1]})
    options.append({agent[0] : agent[1]})
    print 'pa : got options : '+str(options)
    return options
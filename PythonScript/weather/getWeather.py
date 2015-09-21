#! /usr/bin/env python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2
import ast
import time

def GetTime(seconds):
    return time.strftime('%Y-%m-%d %T', time.localtime(seconds))

# definition
city_name = '上海'
base_url = 'http://apis.baidu.com/apistore/weatherservice/citylist?cityname={}&appkey=1307ee261de8bbcf83830de89caae73f'.format(urllib.quote(city_name))
api_key = 'd38050fa70ee7cca921cfeb42ca58cda'

# Query data
request = urllib2.Request(base_url)
request.add_header('apikey', api_key)
content = urllib2.urlopen(request).read()
print content

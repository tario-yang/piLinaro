#! /usr/bin/env python
# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2
import ast
import time

error_code = {
    '300201' : 'URL cannot be resolved',
    '300202' : 'Missing apikey',
    '300203' : 'Apikey or secretkey is NULL',
    '300204' : 'Apikey does not exist',
    '300205' : 'Api does not exist',
    '300206' : 'Api out of service',
    '300301' : 'Internal error',
    '300302' : 'Sorry. The system is busy. Please try again later.'
}

oil_type = {
    'oil93' : '92号汽油',
    'oil97' : '95号汽油'
}

def GetOilTypeName(oilType):
    if oil_type.haskey(oilType):
        return oil_type[oilType]
    else:
        return oilType

def GetTime(seconds):
    return time.strftime('%Y-%m-%d %T', time.localtime(seconds))

# definition
province = '上海'
base_url = 'http://apis.baidu.com/netpopo/oil/oil?province={}&appkey=1307ee261de8bbcf83830de89caae73f'.format(urllib.quote(province
))
api_key = 'd38050fa70ee7cca921cfeb42ca58cda'

# Query data
request = urllib2.Request(base_url)
request.add_header('apikey', api_key)
content = urllib2.urlopen(request).read()
#print content
content = ast.literal_eval(content)

# Output
print 'Province : ', content.get('province')
print '{} : RMB {}'.format(oil_type.get('oil93'), content.get('oil93'))
print '{} : RMB {}'.format(oil_type.get('oil97'), content.get('oil97'))

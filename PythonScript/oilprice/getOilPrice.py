# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2
import ast
import time

if len(sys.argv) == 1:
    province = '上海'
elif len(sys.argv) == 2:
    province = sys.argv[1]
else:
    sys.exit(1)

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

base_url = 'http://apis.baidu.com/netpopo/oil/oil?province={}'.format(urllib.quote(province))
api_key = 'd38050fa70ee7cca921cfeb42ca58cda'

# Query data
request = urllib2.Request(base_url)
request.add_header('apikey', api_key)
content = urllib2.urlopen(request).read()
content = ast.literal_eval(content)

# Output
print content.get('province')
print '\t{} : RMB {}'.format(oil_type.get('oil93'), content.get('oil93'))
print '\t{} : RMB {}'.format(oil_type.get('oil97'), content.get('oil97'))


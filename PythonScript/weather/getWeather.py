# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2
import ast
import time

try:
    data_type = sys.argv[1]
except:
    data_type = 'MORE'
finally:
    try:
        city_name = sys.argv[2]
    except:
        city_name = 'shanghai'

def FetchValueFromDict(objDict, key):
    if isinstance(objDict, dict):
        return objDict.get(key, 'None')
    else:
        return 'None'

def ExceptionCheck(obj):
    if obj is None:
        print 'Nothing found'
        sys.exit(1)

# definition
base_url = 'http://apis.baidu.com/heweather/weather/free?city={}'.format(city_name)
api_key = 'd38050fa70ee7cca921cfeb42ca58cda'

basic = { #城市基本信息
    'city':'城市名称',
    'id':'城市ID',
    'cnty':'国家名称',
    'lat':'纬度',
    'lon':'经度',
    'update':'数据更新时间,24小时制',
    'loc':'数据更新的当地时间',
    'utc':'数据更新的UTC时间',
}

aqi = { #空气质量指数
    'city':'城市数据',
    'aqi':'空气质量指数',
    'pm25':'PM2.5 1小时平均值(ug/m³)',
    'pm10':'PM10 1小时平均值(ug/m³)',
    'so2':'二氧化硫1小时平均值(ug/m³)',
    'no2':'二氧化氮1小时平均值(ug/m³)',
    'co':'一氧化碳1小时平均值(ug/m³)',
    'o3':'臭氧1小时平均值(ug/m³)',
    'qlty':'空气质量类别',
}

suggestion = { #生活指数
    'drsg':'穿衣指数',
    'uv':'紫外线指数',
    'cw':'洗车指数',
    'trav':'旅游指数',
    'flu':'感冒指数',
    'sport':'运动指数',
    'brf':'简介',
    'txt':'详情',
}

alarms = { #灾害预警
    'title':'标题',
    'type':'类型',
    'level':'级别',
    'stat':'状态',
    'txt':'描述',
}

now = { #实况天气
    'tmp':'当前温度(摄氏度)',
    'fl':'体感温度',
    'wind':'风力状况',
    'spd':'风速(Kmph)',
    'sc':'风力等级',
    'deg':'风向(角度)',
    'dir':'风向(方向)',
    'cond':'天气状况',
    'code':'天气代码',
    'txt':'天气描述',
    'pcpn':'降雨量(mm)',
    'hum':'湿度(%)',
    'pres':'气压',
    'vis':'能见度(km)',
}

daily_forecast = { #天气预报
    'date':'当地日期',
    'astro':'天文数值',
    'sr':'日出时间',
    'ss':'日落时间',
    'tmp':'温度',
    'max':'最高温度(摄氏度)',
    'min':'最低温度(摄氏度)',
    'wind':'风力状况',
    'spd':'风速(Kmph)',
    'sc':'风力等级',
    'deg':'风向(角度)',
    'dir':'风向(方向)',
    'cond':'天气状况',
    'code_d':'白天天气代码',
    'txt_d':'白天天气描述',
    'code_n':'夜间天气代码',
    'txt_n':'夜间天气描述',
    'pcpn':'降雨量(mm)',
    'pop':'降水概率',
    'hum':'湿度(%)',
    'pres':'气压',
    'vis':'能见度(km)',
}

hourly_forecast = { #天气预报
    'date':'当地日期和时间',
    'tmp':'当前温度(摄氏度)',
    'wind':'风力状况',
    'spd':'风速(Kmph)',
    'sc':'风力等级',
    'deg':'风向(角度)',
    'dir':'风向(方向)',
    'cond':'天气状况',
    'code_d':'白天天气代码',
    'txt_d':'白天天气描述',
    'code_n':'夜间天气代码',
    'txt_n':'夜间天气描述',
    'pop':'降水概率',
    'hum':'湿度(%)',
    'pres':'气压',
}

error_code = { #错误代码
    'ok':'接口正常',
    'invalid key':'错误的用户 key',
    'unknown city':'未知城市',
    'no more requests':'超过访问次数',
    'anr':'服务无响应或超时',
    'permission denied':'没有访问权限',
}


# Query data
request = urllib2.Request(base_url)
request.add_header('apikey', api_key)
content = urllib2.urlopen(request).read()
content = ast.literal_eval(content)

# Output
output = content['HeWeather data service 3.0'][0]
if output['status'].upper() == 'OK':
    print
    print error_code[output['status']]
    print

    # basic
    output_basic = output.get('basic', None)
    ExceptionCheck(output_basic)
    print '{0}:{1}'.format(basic['id'],   FetchValueFromDict(output_basic, 'id'))
    print '{0}:{1}/{2}'.format(basic['city'],
        FetchValueFromDict(output_basic, 'city'),
        FetchValueFromDict(output_basic, 'cnty'))
    print '{0}:{1}'.format(basic['lat'],  FetchValueFromDict(output_basic, 'lat'))
    print '{0}:{1}'.format(basic['lon'],  FetchValueFromDict(output_basic, 'lon'))
    print '{0}:{1}'.format(basic['loc'],  FetchValueFromDict(output_basic['update'], 'loc'))
    print

    # now
    output_now = output.get('now', None)
    ExceptionCheck(output_now)
    print '{0}:{1}'.format(now['tmp'], FetchValueFromDict(output_now, 'tmp'))
    print '{0}:{1}'.format(now['hum'], FetchValueFromDict(output_now, 'hum'))
    print '{0}:{1}'.format(now['fl'], FetchValueFromDict(output_now, 'fl'))
    print '{0}:{1}'.format(now['pcpn'], FetchValueFromDict(output_now, 'pcpn'))
    print now['wind']
    print '\t{}:{}'.format(now['sc'],  FetchValueFromDict(output_now['wind'], 'sc'))
    print '\t{}:{}'.format(now['spd'], FetchValueFromDict(output_now['wind'], 'spd'))
    print '\t{}:{}'.format(now['dir'], FetchValueFromDict(output_now['wind'], 'dir'))
    print '\t{}:{}'.format(now['deg'], FetchValueFromDict(output_now['wind'], 'deg'))
    print '{0}:{1}'.format(now['pres'], FetchValueFromDict(output_now, 'pres'))
    print '{0}:{1}'.format(now['vis'], FetchValueFromDict(output_now, 'vis'))
    print '{0}:{1}'.format(now['txt'], FetchValueFromDict(output_now['cond'], 'txt'))
    print

    # aqi
    output_aqi = output.get('aqi', None)
    ExceptionCheck(output_aqi)
    output_aqi = output_aqi.get('city', None)
    ExceptionCheck(output_aqi)
    print '{0}:{1}'.format(aqi['qlty'], FetchValueFromDict(output_aqi, 'qlty'))
    print '{0}:{1}'.format(aqi['aqi'], FetchValueFromDict(output_aqi, 'aqi'))
    print '{0}:{1}'.format(aqi['pm25'], FetchValueFromDict(output_aqi, 'pm25'))
    print '{0}:{1}'.format(aqi['pm10'], FetchValueFromDict(output_aqi, 'pm10'))
    print '{0}:{1}'.format(aqi['co'], FetchValueFromDict(output_aqi, 'co'))
    print '{0}:{1}'.format(aqi['so2'], FetchValueFromDict(output_aqi, 'so2'))
    print '{0}:{1}'.format(aqi['o3'], FetchValueFromDict(output_aqi, 'o3'))
    print '{0}:{1}'.format(aqi['no2'], FetchValueFromDict(output_aqi, 'no2'))
    print

    # suggestion
    output_suggestion = output.get('suggestion', None)
    ExceptionCheck(output_suggestion)
    for i in ['drsg', 'uv', 'cw', 'trav', 'flu', 'sport']:
        print suggestion[i]
        tmp = output_suggestion[i]
        print '\t{0}:{1}'.format(suggestion['brf'], FetchValueFromDict(tmp, 'brf'))
        print '\t{0}:{1}'.format(suggestion['txt'], FetchValueFromDict(tmp, 'txt'))
    print

    if data_type == 'MORE':

        # hourly_forecast
        output_hourly_forecast = output.get('hourly_forecast', None)
        ExceptionCheck(output_hourly_forecast)
        for i in output_hourly_forecast:
            print '{0}:{1}'.format(hourly_forecast['tmp'], FetchValueFromDict(i, 'tmp'))
            print '{0}:{1}'.format(hourly_forecast['hum'], FetchValueFromDict(i, 'hum'))
            print '{0}:{1}'.format(hourly_forecast['pop'], FetchValueFromDict(i, 'pop'))
            print hourly_forecast['wind']
            print '\t{}:{}'.format(hourly_forecast['sc'],  FetchValueFromDict(i['wind'], 'sc'))
            print '\t{}:{}'.format(hourly_forecast['spd'], FetchValueFromDict(i['wind'], 'spd'))
            print '\t{}:{}'.format(hourly_forecast['dir'], FetchValueFromDict(i['wind'], 'dir'))
            print '\t{}:{}'.format(hourly_forecast['deg'], FetchValueFromDict(i['wind'], 'deg'))
        print

        # daily_forecast
        output_daily_forecast = output.get('daily_forecast', None)
        ExceptionCheck(output_daily_forecast)
        for i in output_daily_forecast:
            print '*'*32
            print
            print '{0}:{1}'.format(daily_forecast['date'], FetchValueFromDict(i, 'date'))
            print daily_forecast['tmp']
            print '\t{0}:{1}'.format(daily_forecast['max'], FetchValueFromDict(i['tmp'], 'max'))
            print '\t{0}:{1}'.format(daily_forecast['min'], FetchValueFromDict(i['tmp'], 'min'))
            print '{0}:{1}'.format(daily_forecast['hum'], FetchValueFromDict(i, 'hum'))
            print '{0}:{1}'.format(daily_forecast['pop'], FetchValueFromDict(i, 'pop'))
            print '{0}:{1}'.format(daily_forecast['pcpn'], FetchValueFromDict(i, 'pcpn'))
            print daily_forecast['wind']
            print '\t{0}:{1}'.format(daily_forecast['sc'], FetchValueFromDict(i['wind'], 'sc'))
            print '\t{0}:{1}'.format(daily_forecast['spd'], FetchValueFromDict(i['wind'], 'spd'))
            print '\t{0}:{1}'.format(daily_forecast['dir'], FetchValueFromDict(i['wind'], 'dir'))
            print '\t{0}:{1}'.format(daily_forecast['deg'], FetchValueFromDict(i['wind'], 'deg'))
            print daily_forecast['astro']
            print '\t{0}:{1}'.format(daily_forecast['sr'], FetchValueFromDict(i['astro'], 'sr'))
            print '\t{0}:{1}'.format(daily_forecast['ss'], FetchValueFromDict(i['astro'], 'ss'))
            print '{0}:{1}'.format(daily_forecast['pres'], FetchValueFromDict(i, 'pres'))
            print '{0}:{1}'.format(daily_forecast['vis'], FetchValueFromDict(i, 'vis'))
            print daily_forecast['cond']
            print '\t{0}:{1}'.format(daily_forecast['code_d'], FetchValueFromDict(i['cond'], 'code_d'))
            print '\t{0}:{1}'.format(daily_forecast['txt_d'], FetchValueFromDict(i['cond'], 'txt_d'))
            print '\t{0}:{1}'.format(daily_forecast['code_n'], FetchValueFromDict(i['cond'], 'code_n'))
            print '\t{0}:{1}'.format(daily_forecast['txt_n'], FetchValueFromDict(i['cond'], 'txt_n'))
            print


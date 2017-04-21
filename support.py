#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import time

# 为了获取session,session里有xsrf
s = requests.session()

# 基本的 url
url = "https://www.zhihu.com/#signin"
login_url = "https://www.zhihu.com/login/phone_num"
captchaURL = 'http://www.zhihu.com/captcha.gif?r=' + str(timestamp) + '&type=login'
headers = {
    "Host":"www.zhihu.com",
    "Referer":"https://www.zhihu.com/",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
}

data = {
    'phone_num ': '17088843854',
    'pass' : '17088843854f',
}


# 获取xsrf
req = s.get(url, headers=headers)
print s.cookies.get(name='_xsrf')
xsrf = s.cookies.get(name='_xsrf')
data['_xsrf'] = xsrf

# 获取验证码
timestamp = int(time.time() * 1000)
print captchaURL
with open('zhihucaptcha.gif', 'wb') as f:
        captchaREQ = s.get(captchaURL, headers=headers)
        print captchaREQ.content
        print 1111
        f.write(captchaREQ.content)
        loginCaptcha = raw_input('input: ')
        print loginCaptcha
        data['captcha'] = loginCaptcha

# data完整参数
print data
login = s.post(login_url, headers=headers, data=data)
print login.text

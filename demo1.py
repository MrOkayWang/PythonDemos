from urllib import request

#发送一个请求
response = request.urlopen('http://www.baidu.com')
print(response.read()) #不是
print(response.read())


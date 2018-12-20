# import requests
# from urllib.parse import urlparse
#
# url='http://www.cwi.nl:80/%7Eguido/Python.html'
# response = requests.get(url, verify = False)
# o = urlparse(url)
#
# print(o.port)
from urllib.request import urlopen
import urllib
var = urllib.request.urlopen('http://www.stackoverflow.com/')

print(var.geturl())
#
#
# from urllib.request import urlopen
# from selenium import webdriver
# import urllib
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
#
#
# try:
#
#     dcap = dict(DesiredCapabilities.PHANTOMJS)
#
#     dcap["phantomjs.page.settings.userAgent"] = (
#         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87")
#
#     try:
#
#         driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])
#
#         site = "http://google.com/"
#         hdr = {
#             'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#             'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#             'Accept-Encoding': 'none',
#             'Accept-Language': 'en-US,en;q=0.8',
#             'Connection': 'keep-alive'}
#
#         req = urllib.request.Request(site, headers=hdr)
#
#         driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
#
#         driver.get(site)
#
#         WebDriverWait(driver, 15)
#
#         html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
#
#         print(html)
#
#     except Exception as e:
#         print( e)
#
#
# except urllib.error.HTTPError as e:
#     print( e.fp.read())


import urllib
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


#
#
# url="https://google.com/"
#
#
# url = str.replace(url, 'https', 'http')
# opener = urllib.request.build_opener()
#
# request = urllib.request.Request(url)
# response = opener.open(request)
#
# if response.geturl() != url:
#     finalurl = response.geturl()
#
#     print(finalurl)
#
#     driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
#
#     driver.get(finalurl)
#
#     WebDriverWait(driver, 15)
#
#     html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')
#
#     print(html)
#



from urllib.request import Request
a = urllib.request.urlopen('http://bit.ly/cXEInp')
print (a.url)


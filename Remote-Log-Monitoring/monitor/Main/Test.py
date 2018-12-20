# # Accept URL
# #URL-Detection
# # Content-Detection
#
#
#
# # libraries
# import urllib
# import validators
# import requests
#
#
#
# def Url_validity(url):
#     pass
#     validation = validators.url(url)
#     if not validation:
#         test_unshorten = 'https://' + url
#         req = urllib.request.Request(test_unshorten)
#         print(req)
#         try:
#             print(urllib.request.urlopen(req))
#         except urllib.error.HTTPError as e:
#             raise e
#     else:
#         print(url)
#
#
#
#
#
#
#
# def main():
#     Url_validity("http://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?" \
#       "symbol=JPASSOCIAT&fromDate=1-JAN-2012&toDate=1-AUG-2012&datePeriod=unselected&hiddDwnld=true")
#
#
# if __name__ == "__main__":
#     main()
import urllib
# import requests
# r = requests.get("http://www.virustotal.com/")
# print (dict(r.headers).get("x-frame-options"))



import urllib.request
import http.client
from urllib.parse import urlparse


class Urlredi:
    def __init__(self, url):
        self.url = url

    def Urlredi(self, url):

        parsed = urlparse(url)
        print(parsed)
        if parsed.scheme == 'https':
            h = http.client.HTTPSConnection(parsed.netloc)
        else:
            h = http.client.HTTPConnection(parsed.netloc)

        resource = parsed.path
        if parsed.query != "":
            resource += "?" + parsed.query
        h.request('HEAD', resource)
        response = h.getresponse()
        if response.status / 100 == 3 and response.getheader('Location'):
            print(response.getheader('Location'))  # changed to process chains of short urls
        else:
            print(url)


def main():
    url = input("please enter the url to be tested")
    # print("md5 would be:"hashlib.md5(url).hexdigest())
    Urlredi(url)


if __name__ == "__main__":
    main()


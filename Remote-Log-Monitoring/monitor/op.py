# from tkinter import *
# from tkinter import ttk
# import time
#
# MAX = 30
#
# root = Tk()
# root.geometry('{}x{}'.format(400, 100))
# progress_var = DoubleVar() #here you have ints but when calc. %'s usually floats
# theLabel = Label(root, text="Sample text to show")
# theLabel.pack()
# progressbar = ttk.Progressbar(root, variable=progress_var, maximum=MAX)
# progressbar.pack(fill=X, expand=1)
#
#
# def loop_function():
#
#     k = 0
#     while k <= MAX:
#     ### some work to be done
#         progress_var.set(k)
#         k += 1
#         time.sleep(0.02)
#         root.update_idletasks()
#     root.after(100, loop_function)
#
# loop_function()
# root.mainloop()
#
# from selenium import webdriver
# import time
# import string
# from selenium.webdriver.common.keys import Keys
# url = 'https://www.financialjuice.com/News/3772381/A-week-end-of-decision-for-Germany.aspx'
#
# print (url.replace("https", "http"))
#
#
# driver = webdriver.PhantomJS()
#
#
# url = driver.get(url)
#
#
# time.sleep(2)
#
# print(driver.current_url)
#
# driver.quit()


from selenium import webdriver
import urllib
from selenium.webdriver.support.wait import WebDriverWait
from urllib.request import Request


def Url_Redirection(url):
    url = str.replace(url, 'https', 'http')
    opener = urllib.request.build_opener()
    request = urllib.request.Request(url)
    response = opener.open(request)
    if response.geturl()!=url:
        finalurl =  response.geturl()

        print(finalurl)

        try:

            dcap = dict(DesiredCapabilities.PHANTOMJS)

            dcap["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87")

            try:

                driver = webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])

                site = "https://bitcointalk.org/"
                hdr = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}

                req = urllib.request.Request(site, headers=hdr)

                driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

                driver.get(site)

                WebDriverWait(driver, 15)

                html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')

                print(html)


            finally:
                pass

        except urllib.error.HTTPError as e:
            print(e.fp.read())

        print(html)
    else:
        print ("nope")

        driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

        driver.get(url)

        WebDriverWait(driver, 15)

        html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')

        print(html)


if __name__ == '__main__':

    Url_Redirection("https://www.google.com")
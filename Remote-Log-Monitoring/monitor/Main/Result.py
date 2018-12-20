from tkinter import *
from selenium import webdriver
import urllib


from urllib.request import Request
import validators

from tkinter import messagebox
import re

from googlesearch import search
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import validators

from urllib.request import Request

import urllib


def URL_results(url):

    global rooturl

    # url validity

    # function definitions



    def redirection(url):

        var = urllib.request.urlopen(url)

        final_redi = var.geturl()

        get_js_rendered(final_redi)

        Automated_google_search(final_redi)



    def test_403(url):

        try:

            dcap = dict(DesiredCapabilities.PHANTOMJS)

            dcap["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 (KHTML, like Gecko) Chrome/15.0.87")

            try:

                webdriver.PhantomJS(desired_capabilities=dcap, service_args=['--ignore-ssl-errors=true'])

                site = url
                hdr = {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                    'Accept-Encoding': 'none',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Connection': 'keep-alive'}

                urllib.request.Request(site, headers=hdr)

                driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

                driver.get(site)

                WebDriverWait(driver, 15)

                driver.find_element_by_tag_name('html').get_attribute('innerHTML')

                return True

            except Exception as e:
                return e


        except urllib.error.HTTPError as e:
            return e.fp.read()





    def test_shorten(url):

        a = urllib.request.urlopen(url)
        newurl = a.url
        validatio = validators.url(url)

        if validatio:
            redirection()
            get_js_rendered(newurl)
            Automated_google_search(newurl)

        else:

            messagebox.showwarning("Warning", "Invalid Url")



    def get_js_rendered(url):

        url = str.replace(url, 'https', 'http')
        opener = urllib.request.build_opener()

        request = urllib.request.Request(url)
        response = opener.open(request)

        if response.geturl() != url:
            finalurl = response.geturl()

            print(finalurl)

            driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

            driver.get(finalurl)

            WebDriverWait(driver, 15)

            html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')

            print(html)



    def Automated_google_search(url):
        for j in search(url, tld="co.in", num=5, stop=1, pause=2):
            print(j)




    # def validity():
    #     regex = re.compile(
    #         r'^https?://'
    #         r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
    #         r'localhost|'
    #         r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    #         r'(?::\d+)?'
    #         r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    #
    #     if regex.search(url):
    #         return True
    #     else:
    #         return Exception



    def validity():

        validation = validators.url(url)

        if not validation:

            test_shorten()

        else:
            return True



    if url is not None:
        if validity():

            redirection(url)
            test_403(url)


            if test_403(url):

                # url = "https://google.com/"

                url = str.replace(url, 'https', 'http')
                opener = urllib.request.build_opener()

                request = urllib.request.Request(url)
                response = opener.open(request)

                if response.geturl() != url:
                    finalurl = response.geturl()

                    print(finalurl)

                    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])

                    driver.get(finalurl)

                    WebDriverWait(driver, 15)

                    html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')

                    print(html)

                    for j in search(url, tld="co.in", num=5, stop=1, pause=2):
                        print(j)

        else:
            test_shorten()
            redirection()

    else:
        messagebox.showwarning("Warning", "Invalid Url")

        if messagebox:

            messagebox.showinfo("Information", "Try Again")
        else:

            rooturl = Tk()

            rooturl.configure(background="lavender")

            Button(rooturl, text='X', command=rooturl.quit, font=("Helvetica", 10), fg='red', bg="white").grid(row=1,
                                                                                                               column=3)

            Label(rooturl, text='Analyzed Result\n', bg="lavender", font=("Helvetica", 16)).grid(row=1, column=1)

            Button(rooturl, text='Automated Url Results', font=("Helvetica", 10), fg='red', bg="white").grid(row=3,
                                                                                                             column=3)
            rooturl.pack_slaves()

            rooturl.mainloop()





def Content_results():
    rooturl = Tk()
    rooturl.configure(background="lavender")

    Button(rooturl, text='X', command=rooturl.quit, font=("Helvetica", 10), fg='red', bg="white").grid(row=1, column=3)

    Label(rooturl, text='Analyzed Result\n', bg="lavender", font=("Helvetica", 16)).grid(row=1, column=1)

    rooturl.pack_slaves()
    rooturl.mainloop()









def Detection_Result():

    rooturl = Tk()

    rooturl.configure(background="lavender")

    Button(rooturl, text='X', command=rooturl.quit, font=("Helvetica", 10), fg='red', bg="white").grid(row=1, column=3)

    Label(rooturl, text='Analyzed Result\n', bg="lavender", font=("Helvetica", 16)).grid(row=1, column=1)

    rooturl.pack_slaves()
    rooturl.mainloop()


def main():
    global root

    root = Tk()

    root.configure(background="lavender")

    Button(root, text='X', command=root.quit, font=("Helvetica", 10), fg='red', bg="white").grid(row=1, column=3)

    Label(root, text='Analyzed Result\n', bg="lavender", font=("Helvetica", 16)).grid(row=1, column=1)
    Label(root, text='URL Result Here ', bg="lavender", font=("Helvetica", 10)).grid(row=2, column=0, sticky=W)

    Label(root, text='Content Result Here ', bg="lavender", font=("Helvetica", 10)).grid(row=4, column=0, sticky=W)
    Label(root, text='Detection Result Here ', bg="lavender", font=("Helvetica", 10)).grid(row=7, column=0, sticky=W)


    Button(root, borderwidth = 4, text='URL results', command=URL_results, font=("Helvetica", 10), fg='#a1dbcd' , bg= "#383a39").grid(row=2, column = 2)

    Button(root, borderwidth = 4, text='Content results', command=Content_results, font=("Helvetica", 10), fg='#a1dbcd' , bg= "#383a39").grid(row=4, column=2)

    Button(root, borderwidth = 4, text='Detection Result Here', command=Detection_Result, font=("Helvetica", 10), fg='#a1dbcd' , bg= "#383a39").grid(row=7, column=2)

    Button(root, borderwidth = 6, text='Details', command=Detection_Result, font=("Helvetica", 10), fg='#a1dbcd' , bg= "#383a39").grid(row=9, column=3)


    root.pack_slaves()
    root.mainloop()


if __name__ == '__main__':
    main()

from selenium import webdriver
import urllib
from urllib.parse import urlparse
from urllib.request import Request
import urllib.request



def Url_Redirection(url):

    driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
    driver.get(url)
    print(driver.current_url)
    html_content = driver.page_source
    print(html_content)



def main():
    Url_Redirection("https://google.com/")



if __name__ == "__main__":
    main()
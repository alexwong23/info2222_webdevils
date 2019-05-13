import requests
import time
import getpass
import selenium
import time
import sys
import csv
import getpass

from selenium import webdriver

#------------------------------------------------

# default_target = "https://canvas.sydney.edu.au/courses/14331/groups#tab-6293"
default_target_webdevils = "https://10.83.67.113"
#------------------------------------------------
# Useage:
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------


def scraper(target):

    driver = webdriver.Firefox()
    groups = {}


    print("Webdevils login creds:")

    print("Loading login portal")
    driver.get("https://10.83.67.113")

    securityFlag = 0

    try:
        security_check = driver.find_element_by_id("advancedButton")
        securityFlag = 1
    except:
        securityFlag = 0

    if securityFlag == 1:
        security_check = driver.find_element_by_id("advancedButton")
        security_check.click()

        security_check2 = driver.find_element_by_id("exceptionDialogButton")
        security_check2.click()


    logo_element = driver.find_element_by_class_name("logo")
    logo_element.click()

    sideBarElement = driver.find_element_by_id("sidebarCollapse")
    #close side bar
    sideBarElement.click()
    time.sleep(1)
    #Open side bar
    sideBarElement.click()
    time.sleep(1)

    try:
        html_element = driver.find_element_by_xpath("//a[@href='#homeSubmenu']")
        html_element.click()
        time.sleep(1)

    except:
        print("cannot find homeSubmenu")

    try:
        html_element = driver.find_element_by_xpath("//a[@href='/content/HTML/Basic-HTML']")
        html_element.click()
        time.sleep(1)
    except:
        print("cannot find basic html")

    #go to Basic Html page
    # driver.get("http://localhost:8080/content/HTML/Basic-HTML")
    driver.back()

    try:
        html_element = driver.find_element_by_xpath("//a[@href='#homeSubmenu']")
        html_element.click()
        time.sleep(1)

    except:
        print("cannot find homeSubmenu")

    try:
        html_element = driver.find_element_by_xpath("//a[@href='/content/HTML/Formatting']")
        html_element.click()
        time.sleep(1)
    except:
        print("cannot find Formatting")

    time.sleep(1)

    try:
        html_element = driver.find_element_by_class_name("content_category")
        html_element.click()
        time.sleep(1)
    except:
        print("cannot find content_category")

    driver.back()

    try:
        html_element = driver.find_element_by_xpath("//a[@href='#pageSubmenu']")
        html_element.click()
        time.sleep(1)

    except:
        print("cannot find #pageSubmenu")

    try:
        html_element = driver.find_element_by_xpath("//a[@href='/content/CSS/Functions']")
        html_element.click()
        time.sleep(1)
    except:
        print("cannot find Functions")

    try:
        html_element = driver.find_element_by_class_name("content_category2")
        html_element.click()
        time.sleep(1)
    except:
        print("cannot find content_category2")



    driver.close()




if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target_webdevils
    else:
        target_url = sys.argv[1]
    scraper(default_target_webdevils)
    # groups = scrape(target_url)
    # csv_groups(groups)
print("Finished!")

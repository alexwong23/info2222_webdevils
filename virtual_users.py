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

    time.sleep(1)


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

    # #user enters password here
    # username = input("Enter your Webdevils username: ")
    # password = getpass.getpass()
    #
    # print("Logging in")
    #
    # # Enter username
    # username_field = driver.find_element_by_name("UserName")
    # username_field.clear()
    # username_field.send_keys(username)
    #
    # # Enter password
    # password_field = driver.find_element_by_name("Password")
    # password_field.clear()
    # password_field.send_keys(password)
    #
    # # Hit the button
    # login_button = driver.find_element_by_id("submitButton")
    # login_button.click()
    #
    # time.sleep(2)
    #
    # print("Logged in!")
    # driver.get(target)
    #
    #


















# def scrape(target):
#
#     driver = webdriver.Firefox()
#     groups = {}
#
#
#     print("Canvas login creds:")
#
#     print("Loading login portal")
#     driver.get("https://canvas.sydney.edu.au/")
#
#     username = input("Enter your canvas username: ")
#     password = getpass.getpass()
#
#     print("Logging in")
#
#     # Enter username
#     username_field = driver.find_element_by_name("UserName")
#     username_field.clear()
#     username_field.send_keys(username)
#
#     # Enter password
#     password_field = driver.find_element_by_name("Password")
#     password_field.clear()
#     password_field.send_keys(password)
#
#     # Hit the button
#     login_button = driver.find_element_by_id("submitButton")
#     login_button.click()
#
#     time.sleep(2)
#
#     print("Logged in!")
#     driver.get(target)
#
#     for group in range(1, 50):
#         try:
#             # Click to expand group header
#             group_xpath = '//*[@class="span9 groups"]//div//ul//li[{group}]//div//div//a'
#             group_heading = driver.find_element_by_xpath(group_xpath.format(group=group))
#             group_name = group_heading.text
#             group_heading.click()
#
#             groups[group_name] = []
#
#             # Get members from group
#             for member in range(1,6):
#                 try:
#                     member_xpath = '//*[@class="span9 groups"]//div//ul//li[{group}]//div[2]//ul//li[{member}]//div'
#                     member_name = driver.find_element_by_xpath(member_xpath.format(group=group, member=member)).text
#
#                     groups[group_name].append(member_name)
#                 except:
#                     print("Member not found")
#         except:
#             pass
#
#         print("Group: {} contains {}".format(group_name, groups[group_name].__repr__()) )
#
#     print("Scraping finished, closing web driver.")
#     driver.close()
#     return groups


#------------------------------------------------

# def csv_groups(groups):
#     with open('groups.csv', 'w') as groups_file:
#         csv_writer = csv.writer(groups_file)
#         for count, group in enumerate(groups):
#             if len(groups[group]) > 0:
#                 for member in groups[group]:
#                     group_line = ['group_{}'.format(count ), member]
#                     csv_writer.writerow(group_line)
#     print("CSV written")
#     return

#------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        target_url = default_target_webdevils
    else:
        target_url = sys.argv[1]
    scraper(default_target_webdevils)
    # groups = scrape(target_url)
    # csv_groups(groups)
print("Finished!")

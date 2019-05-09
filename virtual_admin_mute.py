import requests
import time
import getpass
import selenium
import time
import sys
import csv
import getpass
import random

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

    print("Webdevils login creds:")
    print("Loading login portal")

    admin ={'admin1':'password'}

    driver.get("https://10.83.67.113")
    time.sleep(1)

    try:
        login_element = driver.find_element_by_xpath("//a[@href='/login']")
        login_element.click()
        time.sleep(1)

    except:
        print("Unable to login")


    for username,password in admin.items():

        #LOG IN AS ADMIN
        try:
            username_field = driver.find_element_by_name("unikey")
            username_field.clear()
            username_field.send_keys(username)

            time.sleep(1)

            password_field = driver.find_element_by_name("password")
            password_field.clear()
            password_field.send_keys(password)

            # Hit the button
            login_button = driver.find_element_by_class_name("inputButton")
            login_button.click()
            time.sleep(2)

        except:
            print("error in logging in")

    try:
        #HIT ADMIN
        changePassword_element = driver.find_element_by_xpath("//a[@href='/users/search']")
        changePassword_element.click()
        #SEARCH FOR ALAN
        searchUser_element = driver.find_element_by_class_name("form-control")
        searchUser_element.clear()
        searchUser_element.send_keys("alan")
        time.sleep(1)

        submit_search = driver.find_element_by_class_name("submit_search")
        submit_search.click()

        #CHANGE STATUS TO MUTE
        banUser_element = driver.find_element_by_id("dropdownMenu2")
        banUser_element.click()

        banUser_element = driver.find_element_by_class_name("option_status_mute")
        banUser_element.click()

        banUser_element = driver.find_element_by_class_name("btn-danger")
        banUser_element.click()
    except:
        print("Unable to mute")

        #LOGOUT
    try:
        logout_button = driver.find_element_by_id("logout_link")
        logout_button.click()
        print("Signup Test complete")
        time.sleep(2)
    except:
        print("Unable to logout")

        #LOGIN AS ALAN
    alan = {'username':'user5',
            'password' : 'password'
            }
    try:
        username_field = driver.find_element_by_name("unikey")
        username_field.clear()
        username_field.send_keys(alan.get('username'))

        time.sleep(1)

        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(alan.get("password"))

            # Hit the button
        login_button = driver.find_element_by_class_name("inputButton")
        login_button.click()
        time.sleep(2)

    except:
        print("error in logging in as Alan")

        #MESSAGE SOMEONE
    try:
        input_string = "//a[@href='/messages']"
        messages_element = driver.find_element_by_xpath(input_string)
        messages_element.click()
        time.sleep(1)

        messagesSearch = driver.find_element_by_xpath("//input[@name='search']")
        messagesSearch.clear()
        messagesSearch.send_keys("Alex")
        time.sleep(1)

        messageSearch_submit = driver.find_element_by_class_name("btn-primary")
        messageSearch_submit.click()
        time.sleep(1)

    #     #Click on Alex
        user_click = driver.find_element_by_class_name("chat_ib")
        user_click.click()

        messages_text = driver.find_element_by_class_name("form-control")
        messages_text.clear()
        messages_text.send_keys("Am I muted now ?")
        time.sleep(1)

        submit_message = driver.find_element_by_class_name("userMessages")
        submit_message.click()
        time.sleep(1)
    except:
        print("Unable to message")



    driver.get(target)
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

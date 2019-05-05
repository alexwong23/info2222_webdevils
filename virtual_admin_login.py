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
default_target_webdevils = "http://localhost:8080"
#------------------------------------------------
# Useage:
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------


def scraper(target):

    driver = webdriver.Firefox()

    admin ={'admin1':'webdevils'}

    alan_account={'user5':'webdevils','user5':'password'}


    print("Webdevils login creds:")

    print("Loading login portal")
    driver.get("http://localhost:8080")

    time.sleep(1)

    try:
        login_element = driver.find_element_by_xpath("//a[@href='/login']")
        login_element.click()
        time.sleep(1)

    except:
        print("Unable to login")

    #Invalid user to login page

    for username,password in admin.items():

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

    #change password_field

    # extract user name
    str = driver.current_url
    str2 = str[28:]

    try:

        changePassword_element = driver.find_element_by_xpath("//a[@href='/users/search']")
        changePassword_element.click()


        searchUser_element = driver.find_element_by_class_name("form-control")
        searchUser_element.clear()
        searchUser_element.send_keys("alan")

        submit_search = driver.find_element_by_class_name("submit_search")
        submit_search.click()


        banUser_element = driver.find_element_by_id("dropdownMenu2")
        banUser_element.click()

        banUser_element = driver.find_element_by_class_name("option_status_ban")
        banUser_element.click()
        #
        banUser_element = driver.find_element_by_class_name("btn-danger")
        banUser_element.click()

        #MESSAGE USER ON BAN

        input_string = "//a[@href='/messages']"
        messages_element = driver.find_element_by_xpath(input_string)
        messages_element.click()


        messagesSearch = driver.find_element_by_xpath("//input[@name='search']")
        messagesSearch.clear()
        messagesSearch.send_keys("alan")

        time.sleep(2)

        messageSearch_submit = driver.find_element_by_class_name("btn-primary")
        messageSearch_submit.click()

        time.sleep(2)

        #Click on Alan fekete
        user_click = driver.find_element_by_class_name("chat_ib")
        user_click.click()


        messages_text = driver.find_element_by_class_name("form-control")
        messages_text.clear()
        messages_text.send_keys("DEAR ALAN, YOU HAVE BEEN BANNED BY THE ADMIN")

        #TODO -> Need to sort out submit button

        submit_message = driver.find_element_by_class_name("userMessages")
        submit_message.click()

    except:
        print("error in admin button")


    try:

        changePassword_element = driver.find_element_by_xpath("//a[@href='/users']")
        changePassword_element.click()


        input_string = "//a[@href='/users/"+str2+"/changepassword']"
        changePassword_element = driver.find_element_by_xpath(input_string)
        changePassword_element.click()
    except:
        print("error in changePassword_element")


    try:
        newpassword_element = driver.find_element_by_name("new_password")
        newpassword_element.clear()
        time.sleep(1)
        newpassword_element.send_keys("password")


        confirmpassword_element = driver.find_element_by_name("confirm_password")
        confirmpassword_element.clear()
        time.sleep(2)
        confirmpassword_element.send_keys("password")

        submit = driver.find_element_by_xpath("//button[@type='submit']")
        submit.click()

        #ADMIN TO logout
        logout_element = driver.find_element_by_id("logout_link")
        logout_element.click()
    except:
        print("error assigning new password")





    for username,password in alan_account.items():
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



    print("Virtual Admin Tasks Complete")
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

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

    print("Webdevils signup creds:")
    print("Loading signup portal")

    driver.get("https://10.83.67.113")
    time.sleep(1)

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

    try:
        signup_element = driver.find_element_by_id("signup_page_button")
        signup_element.click()
        time.sleep(1)

    except:
        print("Unable to signup")

#----------------------------------------------------------------------
#TEST SIGNUP WITH DIFFERENT PASSWORD
    different_password = {
    'unikey' : 'aeio1234',
    'first_name' : 'Kris',
    'last_name' : 'Wu',
    'password' : '12345678',
    'confirm' : '12341234'
    }
    try:
        #FILL IN DETAILS
        unikey_field = driver.find_element_by_name("signup_unikey")
        unikey_field.clear()
        unikey_field.send_keys(different_password.get("unikey"))
        time.sleep(1)

        first_field = driver.find_element_by_name("signup_first_name")
        first_field.clear()
        first_field.send_keys(different_password.get("first_name"))

        time.sleep(1)
        last_field = driver.find_element_by_name("signup_last_name")
        last_field.clear()
        last_field.send_keys(different_password.get("last_name"))

        time.sleep(1)

        password_field = driver.find_element_by_name("signup_password")
        password_field.clear()
        password_field.send_keys(different_password.get("password"))

        time.sleep(1)


        confirm_field = driver.find_element_by_name("signup_confirm_password")
        confirm_field.clear()
        confirm_field.send_keys(different_password.get("confirm"))

        time.sleep(1)

        #HIT SUBMIT
        signup_submit = driver.find_element_by_id("signup_submit_button")
        signup_submit.click();

        time.sleep(2)

    except:
        print("Unable to sign up with different password")


#----------------------------------------------------------------------
#TEST USER EXIST

    exist_virtual = {
    'unikey' : 'abcd1234',
    'first_name' : 'Kris',
    'last_name' : 'Wu',
    'password' : '12345678',
    'confirm' : '12345678'
    }

    try:
        #FILL IN DETAILS
        unikey_field = driver.find_element_by_name("signup_unikey")
        unikey_field.clear()
        unikey_field.send_keys(exist_virtual.get("unikey"))
        time.sleep(1)

        first_field = driver.find_element_by_name("signup_first_name")
        first_field.clear()
        first_field.send_keys(exist_virtual.get("first_name"))

        time.sleep(1)
        last_field = driver.find_element_by_name("signup_last_name")
        last_field.clear()
        last_field.send_keys(exist_virtual.get("last_name"))

        time.sleep(1)

        password_field = driver.find_element_by_name("signup_password")
        password_field.clear()
        password_field.send_keys(exist_virtual.get("password"))

        confirm_field = driver.find_element_by_name("signup_confirm_password")
        confirm_field.clear()
        confirm_field.send_keys(exist_virtual.get("confirm"))

        time.sleep(1)
        #HIT SUBMIT
        signup_submit = driver.find_element_by_id("signup_submit_button")
        signup_submit.click();

        time.sleep(2)

    except:
        print("Unable sign up already exist users")

#----------------------------------------------------------------
#SIGNUP AS A NEW USER
    x = random.randint(1,10001)

    strUser = 'info' + str(x)

    print('your user name is' + strUser)

    new_virtual = {'unikey' : strUser,
    'first_name' : 'Kris',
    'last_name' : 'Wu',
    'password' : '12345678',
    'confirm' : '12345678'
    }
    try:

        #FILL IN DETAILS
        unikey_field = driver.find_element_by_name("signup_unikey")
        unikey_field.clear()
        unikey_field.send_keys(new_virtual.get("unikey"))
        time.sleep(1)

        first_field = driver.find_element_by_name("signup_first_name")
        first_field.clear()
        first_field.send_keys(new_virtual.get("first_name"))


        time.sleep(1)
        last_field = driver.find_element_by_name("signup_last_name")
        last_field.clear()
        last_field.send_keys(new_virtual.get("last_name"))

        time.sleep(1)

        password_field = driver.find_element_by_name("signup_password")
        password_field.clear()
        password_field.send_keys(new_virtual.get("password"))

        time.sleep(1)

        confirm_field = driver.find_element_by_name("signup_confirm_password")
        confirm_field.clear()
        confirm_field.send_keys(new_virtual.get("confirm"))

        time.sleep(1)

        #HIT SUBMIT
        signup_submit = driver.find_element_by_id("signup_submit_button")
        signup_submit.click();

        time.sleep(2)

    except:
        print("Unable sign up new user")
#--------------------------------------------------------------

    #LOGIN
    try:
        password_field = driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(new_virtual.get("password"))
        time.sleep(1)
        # Hit the button
        login_button = driver.find_element_by_class_name("inputButton")
        login_button.click()
        time.sleep(2)
    except:
        print("Unable to login")

    #LOGOUT
    try:
        logout_button = driver.find_element_by_id("logout_link")
        logout_button.click()
        print("Signup Test complete")
        time.sleep(2)
    except:
        print("Unable to logout")


#------------------------------------------
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

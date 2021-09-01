#! /usr/bin/python3
import random
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

###################################
# PROGRAMMA BOT PER INSTAGRAM
###################################
# Global Variables
while_popup_closed = 0
selection_ok = 0
selection = 0
can_proceed = 0
# Comment file inclusion
in_file_comment = open("comment_InstaBot", "r")
ListaCommenti = in_file_comment.readlines()
in_file_comment.close()
# ITag file inclusion
in_file_tag = open("tag_InstaBot", "r")
listaTag = in_file_tag.readlines()
in_file_tag.close()
# User and Password file inclusion
in_file_usrpwd = open("userpwd_InstaBot", "r")
listaUsrPwd = in_file_usrpwd.readlines()
in_file_usrpwd.close()
username_tmp = str(listaUsrPwd[0])
username = username_tmp.strip("username: ")
password_tmp = str(listaUsrPwd[1])
password = password_tmp.strip("password: ")


# FUNCTIONS
def insert_in_search_field(tag_to_search):
    """Insert a tag on search field and click on Enter"""
    Search_Input.send_keys(tag_to_search)
    sleep(20)
    Search_Input.click()
    Search_Input.send_keys(Keys.ENTER)
    Search_Input.click()
    Search_Input.send_keys(Keys.RETURN)
    sleep(5)


def cliccafoto():
    """Function that click on first photo in tag page"""
    First_Photo.click()
    sleep(5)


def put_like():
    """Put a like"""
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)")))
    like = browser.find_element_by_css_selector(
        ".fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)")
    #like.click()  # comment this line to not put a like
    sleep(1)


def insert_comment():
    """Add a random comment chosen from  comment_InstaBot file"""
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Ypffh")))
    sleep(2)
    textarea = browser.find_element_by_class_name("Ypffh")
    textarea.clear()
    textarea.click()
    textarea = browser.find_element_by_class_name("Ypffh")
    random_comment = random.choice(ListaCommenti)
    textarea.send_keys(random_comment)
    sleep(3)
    public_button = browser.find_element_by_css_selector("button.sqdOP:nth-child(4)")
    #public_button.click()  # comment this line if you want to debug and not put a comment
    sleep(3)


def follow():
    """Follow user and save its name"""
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")))
    follow_button = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/header/div[2]/div[1]/div[2]/button")
    #follow_button.click() # comment this line if you want to debug and not follow any user
    sleep(2)
    user_to_save = browser.find_element_by_css_selector(".e1e1d > span:nth-child(1) > a:nth-child(1)")
    user_to_save_name = user_to_save.get_attribute("href")
    print("New follower: " + user_to_save_name)
    in_file_follower = open("follower_InstaBot", "a")
    in_file_follower.write(user_to_save_name + "\n")
    in_file_follower.close()


def unfollow(follower):
    """Unfollow all user in follow_InstaBot file"""
    sleep(2)
    browser.get(follower)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div")))
    unfollow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div")
    unfollow_button.click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[1]")))
    unfollow_button = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
    unfollow_button.click()
    sleep(3)
    print("The user " +follower+ "has been unfollowed\n")


os.system('cls' if os.name == 'nt' else 'clear')


print("*************************************************************************\n"
      "*************************************************************************\n"
      "**********************         INSTA BOT          ***********************\n"
      "*************************************************************************\n"
      "************************************************* Author: Alcarohtar ****\n"
      "*************************************************************************\n"
      "** SELECT AN OPTION: ****************************************************\n"
      "*************************************************************************\n"
      "- 1: Put a like\n"
      "- 2: Put a comment\n"
      "- 3: Like and comment on the photos\n"
      "- 4: Put a like and follow user\n"
      "- 5: Put a comment and follow user\n"
      "- 6: Unfollow user in follow_InstaBot file\n"
      "*************************************************************************\n"
      "*************************************************************************"
      )

while selection_ok == 0:
    try:
        selection = int(input(">>> "))
        print("\n")
        if selection > 6 or selection < 1:
            print("Selection is out of range, insert a number from 1 to 6")
            selection_ok = 0
        else:
            selection_ok = 1
    except:
        print("The choice is not correct, try again with a number from 1 to 6")
        selection_ok = 0


if selection != 6:
    print("*************************************************************************")
    print("** How many photos for every tag do you want to comment or add a like? **")
    print("*************************************************************************")
    num_photo_showed = int(input(">>> "))
    print("\n")
    print("Ok, let's go...")
    print("\n")
else:
    num_photo_showed=0
    print("Ok, let's go...")
    print("\n")


# Init webdriver
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
sleep(5)
# username = input("Insert your username: ")
# password = input("Insert the password: ")

print("I'm closing all popup")

try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/button[1]")))
    Cookie = browser.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    Cookie.click()
    print("Cookie popup has been closed")
except:
    print("Cookie popup was already closed")

sleep(6)
usernameInput = browser.find_elements_by_class_name("_2hvTZ")[0]
password_Input = browser.find_elements_by_class_name("_2hvTZ")[1]
LogIn_Input = browser.find_elements_by_class_name("Igw0E")[0]

usernameInput.send_keys(username)
password_Input.send_keys(password)
LogIn_Input.click()

sleep(6)

# This while is useful to close the all the popup, if needed
while not (can_proceed and (
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cGcGK > div:nth-child(2) > div:nth-child(1)")))):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.sqdOP:nth-child(1)")))
        SalvareLeInfo = browser.find_element_by_css_selector("button.sqdOP:nth-child(1)")
        SalvareLeInfo.click()
        print("Save the Info popup has been closed")
    except:
        print("Save the Info popup was already closed")

    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.aOOlW:nth-child(2)")))
        AttivaLeNotifiche = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        AttivaLeNotifiche.click()
        print("Enable notification popup has been closed")
    except:
        print("Enable notification popup was already closed")

    try:
        Homepage = browser.find_element_by_css_selector(".cGcGK > div:nth-child(2) > div:nth-child(1)").is_displayed()
        can_proceed = 1
        print(".............")
        print("..........")
        print("...done\n")
    except:
        can_proceed = 0
        while_popup_closed += 1

    if while_popup_closed > 3:
        browser.quit()
        print("Something was wrong. Please check the _InstaBot files.")
        exit()

sleep(2)

TagNumber = len(listaTag)

if selection != 6:
    for i in listaTag:
        print("Tag " + i + "is running\n")
        j = 0
        Search_Input = browser.find_elements_by_class_name("XTCLo")[0]
        insert_in_search_field(i)
        element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Nnq7C")))
        First_Photo = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]")
        cliccafoto()
        if selection == 1:
            while j < num_photo_showed:
                put_like()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
                RightArrow = browser.find_element_by_css_selector("._65Bje")
                RightArrow.click()
                j += 1
        elif selection == 2:
            while j < num_photo_showed:
                insert_comment()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
                RightArrow = browser.find_element_by_css_selector("._65Bje")
                RightArrow.click()
                j += 1
        elif selection == 3:
            while j < num_photo_showed:
                put_like()
                insert_comment()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
                RightArrow = browser.find_element_by_css_selector("._65Bje")
                RightArrow.click()
                j += 1
        elif selection == 4:
            while j < num_photo_showed:
                put_like()
                follow()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
                RightArrow = browser.find_element_by_css_selector("._65Bje")
                RightArrow.click()
                j += 1
        elif selection == 5:
            while j < num_photo_showed:
                insert_comment()
                follow()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
                RightArrow = browser.find_element_by_css_selector("._65Bje")
                RightArrow.click()
                j += 1
        else:
            print("Selection out of range")

        sleep(5)
        browser.get('https://www.instagram.com/')

else: #selection == 6
    in_file_follower = open("follower_InstaBot", "r")
    list_follower = in_file_follower.readlines()
    in_file_follower.close()
    for follower in list_follower:
        unfollow(follower)
    in_file_follower = open("follower_InstaBot", "w")
    in_file_follower.close()


print("******* B.O.T. SUCCESSFUL **********")
browser.close()

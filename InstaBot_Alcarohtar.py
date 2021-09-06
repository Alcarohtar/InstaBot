#! /usr/bin/python3
import random
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
from tkinter.ttk import *

###################################
#          INSTAGRAM BOT
###################################
# Global Variables
while_popup_closed = 0
selection_ok = 0
selection = 0
can_proceed = 0

choices = ['1: Put a like',
      '2: Put a comment',
      '3: Like and comment on the photos',
      '4: Put a like and follow users',
      '5: Put a comment and follow users',
      '6: Unfollow users in follow_InstaBot file']

# Comment file inclusion
in_file_comment = open("comment_InstaBot", "r")
ListaCommenti = in_file_comment.readlines()
in_file_comment.close()
# Tag file inclusion
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
def closeAll():
    exit()

def createGUI(windows_tkinter):
    """Tkinter GUI creation"""
    # Nuova finestra tkinter
    windows_tkinter.title('InstaBot Alcarohtar')
    style = Style()
    style.configure('Run.TButton', background='#0e6b03')
    style.configure('info_label_1.TLabel', background='#000000', foreground='#000000')
    # Label
    info_label_1 = Label(windows_tkinter, background='#ffffff',
                         text="- Write in first box the number of photos for each tag you want to analyze\n"
                              "- Select in second box the action to perform\n"
                              "- Press RUN button to start or X to exit from the program\n"
                              "- Once program has started close the browser if you want to abort\n")
    info_label_1.grid(row=5, column=0, pady=14)
    choices_box_label = Label(windows_tkinter, background='#ffffff', font=('Helvetica', 10, 'bold'),
                              text="SELECT AN OPTION")
    choices_box_label.grid(row=3, column=1)
    tb_num_photo_label = Label(windows_tkinter, background='#ffffff', font=('Helvetica', 10, 'bold'),
                               text="NUMBER OF PHOTOS")
    tb_num_photo_label.grid(row=1, column=1)
    info_label_1 = Label(windows_tkinter, background='#000000', width=50, foreground='#a61022', font=('Helvetica', 10, 'bold'),
                         text="\n"
                              " DEVELOPER: Alcarohtar (Luigi Rocco) \n"
                              "", anchor='center')
    info_label_1.grid(row=5, column=1, pady=10, padx=10)
    # Number of photos box
    tb_num_photo = Entry(windows_tkinter, width=42)
    tb_num_photo.insert(0, 1)
    tb_num_photo.grid(row=2, column=1)
    # Option box
    def_var_choices = StringVar(windows_tkinter)
    def_var_choices.set(choices[0])
    choices_box = Combobox(windows_tkinter, textvariable=def_var_choices, values=choices, width=41)
    choices_box['state'] = 'readonly'
    choices_box.grid(row=4, column=1, padx=20)
    # Proceed button
    proceed_button = Button(windows_tkinter, style="Run.TButton", text="RUN", command=windows_tkinter.quit)
    proceed_button.grid(row=1, column=0, rowspan=4, padx=20, ipadx=200, ipady=30)
    windows_tkinter.protocol('WM_DELETE_WINDOW', closeAll)
    windows_tkinter.mainloop()
    choices_box_number = choices_box.get()
    selected_option = int((choices.index(choices_box_number)) + 1)
    tb_num_photo_showed = int(tb_num_photo.get())
    print(selected_option)
    print(tb_num_photo_showed)
    print("\n")
    return selected_option, tb_num_photo_showed


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
    like.click()  # comment this line to not put a like
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
    public_button.click()  # comment this line if you want to debug and not put a comment
    sleep(3)


def follow():
    """Follow user and save its name"""
    follower_just_added = 0
    user_to_save = browser.find_element_by_css_selector(".e1e1d > span:nth-child(1) > a:nth-child(1)")
    user_to_save_name = user_to_save.get_attribute("href")
    in_file_follower_hist = open("follower_history_InstaBot", "r")
    list_hist_follower = in_file_follower_hist.readlines()
    in_file_follower_hist.close()
    for hist_follow in list_hist_follower:
        if hist_follow.rstrip("\n") != user_to_save_name:
            continue
        else:
            follower_just_added = 1
            print("User "+user_to_save_name+" already present in our list. Not added")
            break
    if follower_just_added == 0:
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/\
                                                    div[2]/div/article/header/div[2]/div[1]/div[2]/button")))
            follow_button = browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/header/\
                                                    div[2]/div[1]/div[2]/button")
            follow_button.click()  # comment this line if you want to debug and not follow any user
            sleep(2)
        except:
            print("User already added")
        else:
            user_to_save = browser.find_element_by_css_selector(".e1e1d > span:nth-child(1) > a:nth-child(1)")
            user_to_save_name = user_to_save.get_attribute("href")
            print("New follower: " + user_to_save_name)
            in_file_follower = open("follower_InstaBot", "a")  #Save the new users in file. This file will be
            in_file_follower.write(user_to_save_name + "\n")   #blanked when unfollow is going to call
            in_file_follower.close()
            in_file_follower_hist = open("follower_history_InstaBot", "a")  #Save the new users in file. This file
            in_file_follower_hist.write(user_to_save_name + "\n")           #will never be blanked since it will be
            in_file_follower_hist.close()                                   #used to not follow again the same user


def unfollow(follower_parameter):
    """Unfollow all user in follow_InstaBot file"""
    sleep(2)
    browser.get(follower_parameter)
    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section/main/div/\
                                                header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div")))
        unfollow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/\
                                                div[1]/div/div[2]/div/span/span[1]/button/div")
        unfollow_button.click()
    except:
        pass
    else:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div/div/div/\
                                                div[3]/button[1]")))
        unfollow_button = browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]")
        unfollow_button.click()
        sleep(3)
        print("The user " + follower_parameter + "has been unfollowed\n")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    windows_gui = Tk()
    selected_option, tb_num_photo_showed = createGUI(windows_gui)

    # START THE BROWSER
    selection = selected_option
    if selection != 6:
        num_photo_showed = tb_num_photo_showed
    else:
        num_photo_showed = 0

    browser = webdriver.Firefox()
    browser.get('https://www.instagram.com/')
    sleep(5)

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


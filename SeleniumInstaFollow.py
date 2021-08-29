#! /usr/bin/python3
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


###################################
### PROGRAMMA BOT PER INSTAGRAM ###
###################################
#Variabili Generiche
selezione_ok=0
PuoiProcedere=0
#Inclusione file dei commenti
in_file_comment = open("comment_InstaFollow", "r")
ListaCommenti=in_file_comment.readlines()
in_file_comment.close()
#Inclusione file dei tag
in_file_tag = open("tag_InstaFollow", "r")
listaTag = in_file_tag.readlines()
in_file_tag.close()
#Inclusione file user e password
in_file_usrpwd = open("userpwd_InstaFollow", "r")
listaUsrPwd = in_file_usrpwd.readlines()
in_file_usrpwd.close()
username_tmp = str(listaUsrPwd[0])
username = username_tmp.strip("username: ")
password_tmp = str(listaUsrPwd[1])
password = password_tmp.strip("password: ")

#FUNZIONI
def InserisciInRicerca(tagDaRicercare):
    '''Inserisce il tag tagDaRicercare nel campo ricerca della homepage e da un invio'''
    RicercaInput.send_keys(tagDaRicercare)
    sleep(20)
    RicercaInput.click()
    RicercaInput.send_keys(Keys.ENTER)
    RicercaInput.click()
    RicercaInput.send_keys(Keys.RETURN)
    sleep(5)

def cliccaFoto():
    '''Clicca sulla prima foto della pagina tag'''
    PrimaFoto.click()
    sleep(5)

def MiPiace():
    '''Mette un mi piace'''
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)")))
    Like = browser.find_element_by_css_selector(".fr66n > button:nth-child(1) > div:nth-child(1) > span:nth-child(1) > svg:nth-child(1)")
    Like.click() #eliminare questa riga per debuggare e non inserire mi piace a caso
    sleep(1)


def Commenta():
    '''Commenta le foto ognuna con un commento preso a caso da una lista'''
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Ypffh")))
    sleep(2)
    TextArea = browser.find_element_by_class_name("Ypffh")
    TextArea.clear()
    TextArea.click()
    TextArea = browser.find_element_by_class_name("Ypffh")
    commentoVariabile = random.choice(ListaCommenti)
    TextArea.send_keys(commentoVariabile)
    sleep(3)
    PubblicaButton = browser.find_element_by_css_selector("button.sqdOP:nth-child(4)")
    PubblicaButton.click() #eliminare questo quando si vuole debuggare e non aggiungere commenti a caso
    sleep(3)

# Inizializzo webdriver
browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')
sleep(5)
#username = input("Inserisci il tuo user: ")
#password = input("Inserisci la tua password: ")

try:
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/button[1]")))
    Cookie = browser.find_element_by_xpath("/html/body/div[4]/div/div/button[1]")
    Cookie.click()
except:
    print("Cookie non presente")

sleep(6)
usernameInput = browser.find_elements_by_class_name("_2hvTZ")[0]
passwInput = browser.find_elements_by_class_name("_2hvTZ")[1]
AccediInput = browser.find_elements_by_class_name("Igw0E")[0]

usernameInput.send_keys(username)
passwInput.send_keys(password)
AccediInput.click()
print("Chiudo tutti i popup aperti")
sleep(6)

#Questo while serve per chiudere, nel caso fossero presenti, tutti i popup
while not (PuoiProcedere and (EC.element_to_be_clickable((By.CSS_SELECTOR, ".cGcGK > div:nth-child(2) > div:nth-child(1)")))):
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.sqdOP:nth-child(1)")))
        SalvareLeInfo = browser.find_element_by_css_selector("button.sqdOP:nth-child(1)")
        SalvareLeInfo.click()
        print("...........")
    except:
        print("...........")

    try:
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.aOOlW:nth-child(2)")))
        AttivaLeNotifiche = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
        AttivaLeNotifiche.click()
        print("...........")
    except:
        print("...........")

    try:
        Homepage = browser.find_element_by_css_selector(".cGcGK > div:nth-child(2) > div:nth-child(1)").is_displayed()
        PuoiProcedere = 1
        print("Ok, let's go...")
    except:
        PuoiProcedere = 0


sleep(2)

print(""
      "Seleziona una delle seguenti opzioni:\n"
      "1: Like a foto\n"
      "2: Commenti a foto\n"
      "3: Like e commenti\n"
      )

while selezione_ok == 0:
    try:
        selezione = int(input(">>>"))
        if selezione > 3 or selezione < 1:
            print("La selezione è fuori range, inserisci un numero da 1 a 3")
            selezione_ok=0
        else:
            selezione_ok=1
    except:
        print("La scelta non è corretta, riprova con un numero da 1 a 3")
        selezione_ok=0


numeroTag = len(listaTag)
numeroFotoDaVisual = int(input("A quante foto per ogni tag vuoi mettere un like o un commento?: "))

for i in listaTag:
    print(i)
    j=0
    RicercaInput = browser.find_elements_by_class_name("XTCLo")[0]
    InserisciInRicerca(i)
    element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "Nnq7C")))
    PrimaFoto = browser.find_elements_by_class_name("v1Nh3")[0]
    cliccaFoto()
    if selezione == 1:
        while j < numeroFotoDaVisual:
            MiPiace()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
            RightArrow = browser.find_element_by_css_selector("._65Bje")
            RightArrow.click()
            j += 1
    elif selezione == 2:
        while j < numeroFotoDaVisual:
            Commenta()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
            RightArrow = browser.find_element_by_css_selector("._65Bje")
            RightArrow.click()
            j += 1
    else:
        while j < numeroFotoDaVisual:
            MiPiace()
            Commenta()
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._65Bje")))
            RightArrow = browser.find_element_by_css_selector("._65Bje")
            RightArrow.click()
            j += 1
    sleep(5)
    browser.get('https://www.instagram.com/')

browser.close()
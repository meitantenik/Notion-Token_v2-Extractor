import selenium         #Is the webscraping framework
import os               # Is used to get the username inorder to get the default profile 
from selenium import webdriver
from tkinter import *
# before running this please make sure chrome is not running in the background with the default profile on
# In this version of the implementation the user must have had already logged in to the  account 
usern = os.getlogin()       #getting the username
doka = f'user-data-dir=C:\\Users\\{usern}\\AppData\\Local\\Google\\Chrome\\User Data'   # opening chrome's default profile 
 
 
ch_options = webdriver.ChromeOptions() 
ch_options.add_argument(doka)       #Path to your chrome profile
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\chromedriver.exe", options=ch_options)
 
 
#getting the cookie 
driver.get("https://notion.so")         #opening Notion
ilist= driver.get_cookie('token_v2')    #searching for the cookie
 
 
    
#searching for the value of the cookie
tokenv2 = {'value'} 
v = [ilist[i] for i in tokenv2 if i in ilist ]
result = v[0]
 
#saving result to file and printing
with open('tokenv2.txt','w') as file:
    file.write(result)
 
driver.quit() #closing chrome 
 
'''
#remove quotation marks in order to print value  window 
window = Tk()
window.title('Your Notion token')
lbl = Label(window, text = result,font=("Arial", 25))
lbl.grid(column=0, row =0)
window.mainloop()
'''

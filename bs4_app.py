import bs4
import requests
from tkinter import *


win = Tk()
win.configure().keys()


def scrapping():
    url = requests.get(URL.get())
    res = bs4.BeautifulSoup(url.text, 'html.parser')
    saveFile1 = open('WEB_TEXT.txt', 'a')
    for i in res.select('p'):
        saveFile1.write(i.getText())
    saveFile1.close()

    saveFile2 = open('WEB_CODE.txt', 'a')
    for r in res.select('p'):
        saveFile2.write(r.prettify())
    saveFile2.close()


var = StringVar()
var.set('WEBSITE SCRAPPER TOOL')

Label(win, textvariable=var, bd=8, bg='yellow', font=("Helvetica", 35)).grid(row=0, column=0)

URL = StringVar()

Entry(win, bd=5, font=7, textvariable=URL).grid(row=1, column=0, ipadx=100)

Button(win, text='Scrap it!', bd=5, command=scrapping).grid(row=2, column=0, padx=8, pady=4)

win.mainloop()

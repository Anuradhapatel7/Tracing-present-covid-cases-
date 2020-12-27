# required module- request,tkintertable,bs4
import requests
from bs4 import BeautifulSoup
from tkinter import *

country = "india"

# url for fatching data
page2 = requests.get('https://www.worldometers.info/coronavirus/')

# for getting page content
Soup2 = BeautifulSoup(page2.content, 'html.parser')

# for finding specific data
info2 = Soup2.find_all(class_="maincounter-number")
root = Tk()
root.title("corona report")
root.geometry("400x550")
font = ("Helvetica", 12, "bold")


# function for getting optionly country data

def btn_click():
    country = c.get()
    page = requests.get('https://www.worldometers.info/coronavirus/country/' + country)
    Soup = BeautifulSoup(page.content, 'html.parser')
    info = Soup.find_all(class_='maincounter-number')

    a = [items.get_text() for items in info]
    ccd = Label(root, font=font, text=country + " Cases of Corona")
    ccd.pack()
    cc = Label(root, font=font, text=a[0])
    cc.pack()
    cdl = Label(root, font=font, text=country + " Cases of Deaths")
    cdl.pack()
    cd = Label(root, font=font, text=a[1])
    cd.pack()
    crl = Label(root, font=font, text=country + " Cases of Recovered")
    crl.pack()
    cr = Label(root, font=font, text=a[2])

    cr.pack()


# this code is for World corona details
b = [items.get_text() for items in info2]
wc = Label(root, font=font, text="World Cases of Corona")
wc.pack()
wc = Label(root, font=font, text=b[0])
wc.pack()
wc = Label(root, font=font, text="World Cases of Deaths")
wc.pack()
wd = Label(root, font=font, text=b[1])
wd.pack()
wc = Label(root, font=font, text="World Cases of Recovered")
wc.pack()
wr = Label(root, font=font, text=b[2])
wr.pack()
wc = Label(root, font=font, text="Enter country name")
wc.pack()
c = Entry(root, font=font)
c.pack()

sendBtn = Button(root, text="Find", command=btn_click, bg="green")

sendBtn.pack()
root.mainloop()

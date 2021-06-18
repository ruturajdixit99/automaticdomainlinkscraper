import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
from tkinter import scrolledtext
import requests
from bs4 import BeautifulSoup
import webbrowser
from googlesearch import search
import bs4
from tkinter import messagebox as mb
from tkinter.ttk import *
import csv

root = tk.Tk()
root.title("Website Links Fetcher")
progress = Progressbar(root, orient = HORIZONTAL,
			length = 100, mode = 'determinate')


root.geometry("1000x1000")
name_var = tk.StringVar()
# nm_var = tk.StringVar()




def delet_text():
    T.delete(0.0, "end")



def submit():
    T.delete(0.0,'end')
    u = name_var.get()
    # u = input("Niche: ")
    ur = "site:yelp.com/biz " + u + "- CLOSED -"
    search_query = ur
    for item in search(search_query,
                       tld='co.in',
                       lang='en',
                       num=15,
                       stop=15,
                       pause=2.0):
        print(item)



        url = item
        data = requests.get(url)
        soup = bs4.BeautifulSoup(data.text, 'html.parser')
        # print(soup.prettify())
        #
        # find link of business website


        for links in soup.find_all('a', {"class": "css-ac8spe"} and {"target": "_blank"}):
            if (links == 'a', {"class": "css-ac8spe"} and {"target": "_blank"}):
                link = links.get('href')
                print(link)

            else:
                print('Not Found')

            lin ="\n\n->>>\n"+""+link
            T.insert(0.0,lin)


        import time
        webbrowser.open_new_tab('https://google.com/search?q= '+link)
        time.sleep(1)


        import time
        progress['value'] = 20
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 40
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 50
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 60
        root.update_idletasks()
        time.sleep(1)

        progress['value'] = 80
        root.update_idletasks()
        time.sleep(1)
        progress['value'] = 100

name_label = tk.Label(root, text='Enter Niche', font=('Arial', 16, 'normal'))
name_entry = tk.Entry(root, textvariable= name_var, font=('Arial Nova', 12, 'normal'))
#
# nm_label = tk.Label(root, text='Save file as', font=('Arial', 16, 'normal'))
# nm_entry = tk.Entry(root, textvariable=nm_var , font=('Arial Nova', 12, 'normal'))

sub_btn = tk.Button(root, text='submit',fg='black',bg='silver',bd=4,font=('Arial'), command=submit)
Button(root, text="Clear All Link's",command=delet_text).grid(row=1,column=1)
# btt = tk.Button(root,text='Save to CSV',command=s)

T = scrolledtext.ScrolledText(root,wrap = tk.WORD,bg='black',fg='yellow',bd='2',height=30,width=100,font=('Times New Roman',14,'normal'))
l = Label(root,text = "WEBSITE LINKS")
l.config(font =("Arial Nova",18))

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
# nm_label.grid(row=2,column=0)
# nm_entry.grid(row=2,column=1)
# btt.grid(row=2,column=2)
sub_btn.grid(row=0, column=4)
l.grid(row=1,column=5,pady=10,padx=50)
T.grid(row=2,column=5,pady=10,padx=10)
progress.grid(row=1,column=4)


T.focus()

root.mainloop()

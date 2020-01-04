# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:04:54 2019

@author: Sucheth
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:01:52 2019

@author: Sucheth
"""
import tkinter as tk
from tkinter import ttk
import webbrowser
import requests 
import bs4

x=0


                                 
                                 
                                 
                                 
win=tk.Tk()
win.title("News Analyser")
Elabel=ttk.Label(win,text="\tEnglish News Paper").grid(column=1,row=0,sticky='nwse')
new = 1

def Hindu_clickMe():
    webbrowser.open("https://www.thehindu.com/todays-paper/")
style=ttk.Style()
style.configure('W.TButton', font =
               ('calibri', 44, 'bold'))           
Hindu_action=ttk.Button(win,text='Hindu',command=Hindu_clickMe)
Hindu_action.grid(column=1,row=1,sticky='nwse')
def TOI_clickMe():
   webbrowser.open("https://timesofindia.indiatimes.com/news")

#adding a button
TOI_action=ttk.Button(win,text='TOI',command=TOI_clickMe)
TOI_action.grid(column=1,row=2,sticky='nwse')
def Deccan_clickMe():
    webbrowser.open("https://www.deccanherald.com/")
             
#adding a button
Deccan_action=ttk.Button(win,text='Deccan',command=Deccan_clickMe)
Deccan_action.grid(column=1,row=3,sticky='nwse')

res=requests.get('https://www.thehindu.com/todays-paper/')
res.text
soup=bs4.BeautifulSoup(res.text,'lxml')

for link in soup.find_all('div',{'class':"tpaper-container"}):
    text1 =link.text

data=[]
str = text1.split()

res=requests.get('https://timesofindia.indiatimes.com')
res.text
soup=bs4.BeautifulSoup(res.text,'lxml')

for link in soup.find_all('div',{'id':"content"}):
    text1 =link.text

data=[]
str1 = text1.split()


res=requests.get('https://www.deccanherald.com')
res.text
soup=bs4.BeautifulSoup(res.text,'lxml')

for link in soup.find_all('div',{'class':"secLightGreen hasBGColor overlapped-container"}):
    text1 =link.text

data=[]
str2 = text1.split()


      	

def clickMe():
    k=0
    for i in str:
        if(i==name.get()):
            k=k+1    
    ttk.Label(win,text='Hindu News Paper').grid(column=0,row=8,sticky='nwse')        
    ttk.Label(win,text="Word").grid(column=0,row=9,sticky='nwse')
    ttk.Label(win,text=name.get()).grid(column=1,row=9,sticky='nwse')
    ttk.Label(win,text='Count Value ').grid(column=0,row=10,sticky='nwse')
    ttk.Label(win,text=k).grid(column=1,row=10,sticky='nwse')
    for i in str1:
        if(i==name.get()):
            k=k+1    
    ttk.Label(win,text='TOI News Paper').grid(column=0,row=11,sticky='nwse')        
    ttk.Label(win,text="Word").grid(column=0,row=12,sticky='nwse')
    ttk.Label(win,text=name.get()).grid(column=1,row=12,sticky='nwse')
    ttk.Label(win,text='Count Value ').grid(column=0,row=13,sticky='nwse')
    ttk.Label(win,text=k).grid(column=1,row=13,sticky='nwse')
    for i in str2:
        if(i==name.get()):
            k=k+1    
    ttk.Label(win,text='Deccan News Paper').grid(column=0,row=14,sticky='nwse')        
    ttk.Label(win,text="Word").grid(column=0,row=15,sticky='nwse')
    ttk.Label(win,text=name.get()).grid(column=1,row=15,sticky='nwse')
    ttk.Label(win,text='Count Value ').grid(column=0,row=16,sticky='nwse')
    ttk.Label(win,text=k).grid(column=1,row=16,sticky='nwse')

ttk.Label(win, text="Enter the word").grid(column=0, row=4,sticky='nwse') # 4
name=tk.StringVar()



nameEntered = ttk.Entry(win, width=12, textvariable=name) # 7
nameEntered.grid(column=0, row=5,sticky='nwse')
       
action=ttk.Button(win,text='Click Me',command=clickMe,style='W.TButton')
action.grid(column=1,row=5,sticky='nwse')


win.mainloop()
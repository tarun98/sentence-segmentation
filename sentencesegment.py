# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 09:36:37 2017

@author: Tarun Jairam

"""



"""
r = urllib.request.urlopen("https://en.wikipedia.org/wiki/Hello").read()
soup = BeautifulSoup(r,"lxml")

soup

from IPython.display import Image
Image('http://www.openbookproject.net/tutorials/getdown/css/images/lesson4/HTMLDOMTree.png')
data = soup.findAll(text=True)

k=soup.find_all('p')

text=[]
for i in k:
    text.append(i.get_text())
    
for i in text:
    if len(i)==0:
        text.remove(i)
a="capisce"
"""


from bs4 import BeautifulSoup
import urllib
import re

a="hello"
def funcc(a):
    url="https://en.wikipedia.org/wiki/"
    url = url+a
    r=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(r,"lxml")
    k=soup.find_all('p')
    
    text=[]
    for i in k:
        text.append(i.get_text())
    tex=[re.sub(r"[[]+\d+[]]","",i) for i in text]
    sentences=[]
    for i in tex:
        sentences.extend(i.split(". "))
    
    #stripping punctuations    
    nopunc=[re.sub(r'[^\w\s]','',s) for s in sentences]
     
    words=[]
    for i in nopunc:
        words.extend(i.split(" "))
    wordcount={}
    for i in words:
        if i in wordcount.keys():
            wordcount[i]= wordcount[i]+1
        else:
            wordcount[i]=1
    print("PLAIN TEXT")
    print(text)
    print("SENTENCES")
    for i in sentences:
        print(i)
        print("\n")
    print("SET OF WORDS WITH NUMBER OF OCCURENCES")
    for i in wordcount.keys():
        print(i,wordcount[i])
    
#!/usr/bin/env python
# coding: utf-8


import subprocess
from datetime import date
import requests
import sys




def get_current_background():
    return subprocess.check_output("gsettings get org.gnome.desktop.background picture-uri",shell=True)





def set_current_background(file):
    command = "gsettings set org.gnome.desktop.background picture-uri "
    command +=file
    #print(command)
    subprocess.call(command,shell=True)

def check_if_already_changed_today(l:str):
    f = open('background_changes.txt','a+')
    f_r = open('background_changes.txt','r')
    today = date.today()
    if str(today) in f_r.read():
        return True
    
    f.write(l+" "+str(today)+"\n")
    return False



if __name__ == "__main__":
    args = sys.argv
    #r = requests.get('https://loremflickr.com/1920/1080');
    r = requests.get('https://picsum.photos/1920/1080')
    #print(r.url)
    if(not r.ok):
        print("not connected")
    
    if("daily" in args):
        if(check_if_already_changed_today(r.url)):
            exit()

    set_current_background(r.url)
    


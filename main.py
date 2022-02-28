import os
import ctypes
from ctypes import wintypes
import requests
import time
import json
import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()
hasTime = False
while hasTime == False :
    try:
        inputN = input("How long should I wait? >>")
        waitTime = int(inputN)
        hasTime = True
    except:
        hasTime = False
def Write():
    f = open("config.txt", "a")
    f.write(filedialog.askdirectory())
    f.close()
def Invalid():
    os.remove("config.txt") 
    Write()
    return open("config.txt", "r").read()
try:
    folder = open("config.txt", "r").read()
except:
    Write()
    folder = open("config.txt", "r").read()


def wall(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    image = image_path
    image_path2 = os.path.join(folder, image)
    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path2, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)


def main():
    image_path = os.path.join(folder)
    try :
        images = os.listdir(image_path)
    except :
       images = os.listdir(Invalid())
    for image in images[:]:
        if not image.endswith(("png", "jpg", "ico", "jpeg")):
             images.remove(image)
    counter = 0
    while counter <= len(images):
        try:
            if counter == len(images)-1:
                wall(images[counter])
                counter = 0
                time.sleep(waitTime)
                continue
            else:
                wall(images[counter])
                counter += 1
                time.sleep(waitTime)
        except Exception as e:
            print(e)
            time.sleep(waitTime)
            continue


main()

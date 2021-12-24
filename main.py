import os
import ctypes
from ctypes import wintypes
import requests
import time
import json
import os
waitTime = 5
drive = "c:\\"
folder = "\\Users\\Raven\\Desktop\\cams\\wallpaper"


def wall(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x0001
    SPIF_SENDWININICHANGE = 0x0002
    image = image_path
    image_path2 = os.path.join(drive, folder, image)
    user32 = ctypes.WinDLL('user32')
    SystemParametersInfo = user32.SystemParametersInfoW
    SystemParametersInfo(SPI_SETDESKWALLPAPER, 0,image_path2, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)

def main():
    image_path = os.path.join(drive, folder)
    images = os.listdir(image_path)
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

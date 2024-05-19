# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:17:57 2024

@author: Aidan
"""

from tkinter import *
import speedtest 
import matplotlib .pyplot as plt
import time

list_download_speed = []
list_upload_speed = []

for i in range(5):
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000,2)
    list_download_speed.append(download_speed)
    
    upload_speed = round(st.upload()/1000000,2)
    list_upload_speed.append(upload_speed)
    time.sleep(60)
    print(list_download_speed)
    print(list_upload_speed)
    
x = [1,2,3,4,5]

plt.plot(x, list_download_speed, label = "Velocidad De Descarga")
plt.plot(x, list_upload_speed, label = "Velocidad De Carga")
plt.title("Velocidad")
plt.legend()
plt.show()
    
    

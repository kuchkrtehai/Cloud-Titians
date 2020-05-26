# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:29:31 2020

@author: Gautam
"""
from gtts import gTTS
import os
file=open("test.txt","r")
myText=file.read().replace("\n"," ")
language='en'


output=gTTS(text=myText,lang=language,slow=False)
output.save("Output.mp3")
file.close()
os.system("start Output.mp3")

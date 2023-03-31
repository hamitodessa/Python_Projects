'''
Created on Mar 30, 2023

@author: hamit
'''

from PyQt5 import uic


with open('untitled.py','w' , encoding="utf-8") as fout:
    uic.compileUi('untitled.ui',fout)
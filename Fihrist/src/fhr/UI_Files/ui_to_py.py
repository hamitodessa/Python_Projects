'''
Created on Apr 2, 2023

@author: hamit
'''

from PyQt5 import uic


with open('Anapencere.py','w' , encoding="utf-8") as fout:
    uic.compileUi('anapencere.ui',fout)
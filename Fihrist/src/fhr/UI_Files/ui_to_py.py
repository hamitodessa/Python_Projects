'''
Created on Apr 2, 2023

@author: hamit
'''

from PyQt5 import uic 


with open('Anapencere.py','w' , encoding="utf-8") as fout:
    uic.compileUi('anapencere.ui',fout)
    
#pyrcc5 C:\Users\hamit\git\Phyton\Fihrist\src\fhr\UI_Files\fih_resources.qrc -o C:\Users\hamit\git\Phyton\Fihrist\src\fhr\UI_Files\fih_resources.py
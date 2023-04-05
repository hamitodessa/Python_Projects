'''
Created on Apr 5, 2023

@author: hamit
'''

from pt.Loglama.Loglama_Interfacee import LoglamaInterface


class diger_deneme_kayit(LoglamaInterface):
    def __init__(self, LogKayitInterface,mesaj):
        self.mesaj = mesaj
        self.listee= LogKayitInterface
    def connect(self):
        for qwe in self.listee:
            qwe.connect(self,self.mesaj)

'''
Created on Apr 1, 2023

@author: hamit
'''

class Fihrist_Access():
    def __init__(self, IFihrist,ILoger):
        self.IDb= IFihrist
        self.log_liste= ILoger
    def baglan(self,mesaj):
        for qwe in self.IDb:
            qwe.baglan(self,mesaj)
        #for qwe in self.log_liste:
        #    qwe.logla(self,mesaj)
    def fih__sifirdan_L(self,user_detail,mesaj, evrak, DIZIN_BILGILERI):
        for qwe in self.IDb:
            qwe.fih__sifirdan_L(self,user_detail)
        for qwe in self.log_liste:
            qwe.logla(self,mesaj, evrak, DIZIN_BILGILERI)
    def fih__sifirdan_S(self,mesaj):
        for qwe in self.IDb:
            qwe.fih__sifirdan_S(self,mesaj)
        

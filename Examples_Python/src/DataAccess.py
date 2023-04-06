'''
Created on Apr 1, 2023

@author: hamit
'''



class Cari_Access():
    def __init__(self, DB_Interface,LG_Interface):
        self._ICari = DB_Interface
        self.listee= LG_Interface
    def connect(self,mesaj,mesaj2):
        for qwe in self._ICari:
            qwe.connect(self,mesaj,mesaj2)
        for qwe in self.listee:
            #if qwe.__class__.__name__ == "Dosya_Yaz":
            #    qwe.connect(self,mesaj)
            #else:
                qwe.connect(self,mesaj)
                
        
      
  
    

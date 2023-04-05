'''
Created on Apr 1, 2023

@author: hamit
'''



class Cari_Access():
    def __init__(self, DB_Interface,LG_Interface):
        self._ICari = DB_Interface
        
        self.listee= LG_Interface
    def sil(self,mesaj):
        print(mesaj)
        for qwe in self._ICari:
            qwe.connect(self)
            
        
        for qwe in self.listee:
            qwe.connect(self)
        
       
       
       
       
       
"""     
  __dict__     
    def kaydet(self, DB_Interface ,Loglama_Interface  ):
       classname = DB_Interface
       x=classname()
       x.connect()
     
       
       clsnm = Loglama_Interface 
       x=clsnm()
       x.connect()
      
"""
        
        
  
    

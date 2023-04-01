'''
Created on Apr 1, 2023

@author: hamit
'''



class Cari_Access():
    def __init__(self, DB_Interface,LG_Interface):
        self._ICari = DB_Interface
        self.x=self._ICari()
        self.listee= LG_Interface
    def sil(self,mesaj):
        print(mesaj)
        self.x.connect()
        for qwe in self.listee:
          # print(qwe)
           qwe.connect(self)
        
       
       
       
       
       
       
       
 #   def kaydet(self, DB_Interface ,Loglama_Interface  ):
 #      classname = DB_Interface
 #      x=classname()
 #      x.connect()
     
       
 #      clsnm = Loglama_Interface 
 #      x=clsnm()
 #      x.connect()
      
    
        
        
  
    

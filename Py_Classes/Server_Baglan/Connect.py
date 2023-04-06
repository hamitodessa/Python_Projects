'''
Created on Apr 6, 2023

@author: hamit
'''

class Connect():
    def __init__(self, IConnection):
        self.ICn = IConnection
        print("qaz" + IConnection.__name__)
    def Server_kontrol_L(self,inst, kull, sifre,  portt):
        return self.ICn.Server_kontrol_L(self,  inst, kull, sifre,  portt)
    def Server_kontrol_S(self,server, inst, kull,  sifre, port):
        return self.ICn.Server_kontrol_S(self, server, inst, kull,  sifre, port)
    def Dosyakontrol_L(self, db, kull, sifre,  inst ,  port):
        return self.ICn.Server_kontrol_L(self,  db, kull, sifre,  inst ,  port)
    def Dosyakontrol_S(self,server, inst, kull,sifre, prog , port):
        return self.ICn.Server_kontrol_L(self,  server, inst, kull,sifre, prog , port)
    
    
    
        
      
         
        
        
       

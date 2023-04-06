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
        
      
         
        
        
       

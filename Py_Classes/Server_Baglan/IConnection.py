'''
Created on Apr 6, 2023

@author: hamit
'''
from abc import *

class IConnection(ABC):
    @abstractmethod
    def Server_kontrol_L(self):
        pass
    def Server_kontrol_S(self):
        pass
    def Dosyakontrol_L(self):
        pass
    def Dosyakontrol_S(self):
        pass

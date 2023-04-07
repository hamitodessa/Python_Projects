'''
Created on Apr 1, 2023

@author: hamit
'''

from abc import *

class IFihristt(ABC):
    @abstractmethod
    def baglan(self):
        pass
    @abstractmethod
    def fih__sifirdan_L(self):
        pass
    @abstractmethod
    def fih__sifirdan_S(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
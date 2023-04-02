'''
Created on Apr 1, 2023

@author: hamit
'''

from abc import *

class IFihristt(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
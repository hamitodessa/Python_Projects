'''
Created on Apr 5, 2023

@author: hamit
'''

from abc import *

class ILogKayitInterface(ABC):
    @abstractmethod
    def logla(self):
        pass
    @abstractmethod
    def log_rapor(self):
        pass

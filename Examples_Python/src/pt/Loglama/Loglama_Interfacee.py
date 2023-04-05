'''
Created on Mar 30, 2023

@author: hamit
'''
from abc import *
class LoglamaInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
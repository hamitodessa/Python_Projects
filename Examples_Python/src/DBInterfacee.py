'''
Created on Mar 30, 2023

@author: hamit
'''
from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
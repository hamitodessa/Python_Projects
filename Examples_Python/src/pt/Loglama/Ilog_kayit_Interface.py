'''
Created on Apr 5, 2023

@author: hamit
'''

from abc import *
class LogKayitInterface(ABC):
   @abstractmethod
   def connect(self):
       pass
   @abstractmethod
   def disconnect(self):
       pass

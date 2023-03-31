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
class Oracle(DBInterface):
   def connect(self):
       print('Connecting to Oracle Database...')
   def disconnect(self):
       print('Disconnecting to Oracle Database...')
class Sybase(DBInterface):
   def connect(self):
       print('Connecting to Sybase Database...')
   def disconnect(self):
       print('Disconnecting to Sybase Database...')   
#dbname=input('Enter Database Name either Oracle or Sybase:')
dbname="Oracle"
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()

d



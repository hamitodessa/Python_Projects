

from DBInterface import DBInterface 
from Oracle import Oracle 

newClass = "Oracle"
classname = globals()[Oracle]

x=classname()
x.connect()
x.disconnect()










#from Oraclee    import  Oracle
#from Sybasee    import  Sybase
import Degiskenler as dgs

classname = dgs.classname
x=classname()
x.connect()
x.disconnect()


#classname = Sybase
#x=classname()
#x.connect()
#x.disconnect()

clsnm = dgs.clsnm
x=clsnm()
x.connect()
x.disconnect()

clsnm = dgs.lgcls
x=clsnm()
x.connect()
x.disconnect()



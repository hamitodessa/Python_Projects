'''
Created on Apr 1, 2023

@author: hamit
'''
from Oraclee    import  Oracle
from Sybasee    import  Sybase
from pt.Loglama.Oraclee import LG_Oracle

from pt.Loglama.MySqll  import  LG_MySql
from pt.Loglama.Mail    import LG_Mail
from pt.Loglama.MsSql_Log import lg_kayitMssql
from pt.Loglama.Sq_Lite import sq_lite
from pt.Loglama.Dosya_Yaz import Dosya_yaz

classname = [Oracle]
clsnm = Sybase

#lgcls = [LG_MySql,LG_Oracle,lg_kayitMssql,sq_lite,Dosya_yaz]
lgcls = [LG_Mail,LG_MySql,Dosya_yaz([sq_lite,lg_kayitMssql,LG_Oracle])]

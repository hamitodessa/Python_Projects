'''
Created on Apr 1, 2023

@author: hamit
'''
from Oraclee    import  Oracle
from Sybasee    import  Sybase
from pt.Loglama.Oraclee import LG_Oracle

from pt.Loglama.MySqll  import  LG_MySql
from pt.Loglama.MsSql_Log import lg_kayitMssql
from pt.Loglama.Sq_Lite import sq_lite
classname = [Oracle]
clsnm = Sybase
#lgcls = [LG_Oracle,LG_MySql,diger_deneme_kayit[lg_kayitMssql]]
lgcls = [LG_MySql,LG_Oracle,lg_kayitMssql,sq_lite]

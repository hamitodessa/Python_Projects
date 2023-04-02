'''
Created on Apr 1, 2023

@author: hamit
'''

#region SURUCU_DOSYA_BILGILERI
SURUCU = "C:/OBS_SISTEM/"
OBS_DOSYA = "OBS_SISTEM_2025.MDB"
LOG_DOSYA = "SQL_LOG.MDB"

#Calisilan Database ler
from fh.Dao_MsSql   import  Ms_Sql
from fh.Dao_MySql   import  MySql
#Loglama Yontemleri
from lg.Dao_Mail_At    import  Maill
from lg.Dao_MsSql    import  Dao_MsSql
from lg.Dao_MySql    import  Dao_MySql
from lg.Dao_SqLite    import  Dao_SqLite
from lg.Dao_Txt    import  Dao_Txt


_ICar = None
_IStok = None
_IKur = None
_IAdres = None
_IKambiyo = None
_IGunluk = None
_ISms = None
_Fihrist = None   

_ICari_Loger = None 
_IKur_Loger = None 
_IAdres_Loger = None 
_IFatura_Loger = None 
_IKambiyo_Loger = None 
_ISms_Loger = None 
_IGunluk_Loger = None 
_IFihrist_Loger = None 
    

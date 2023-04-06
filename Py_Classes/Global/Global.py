'''
Created on Apr 1, 2023

@author: hamit
'''
    
#region SURUCU_DOSYA_BILGILERI
SURUCU = "C:/OBS_SISTEM/"
OBS_DOSYA = "OBS_SISTEM_2025.DB"
OBS_FIHRIST_DOSYA = "FIHRIST.DB"
LOG_DOSYA = "SQL_LOG.MDB"
DBYERI = "C:/OBS_DATABASES/"

#Calisilan Database ler
from fh.Dao_MsSql   import  Ms_Sql
from fh.Dao_MySql   import  MySql
#Loglama Yontemleri
from lg.Dao_Mail_At    import  Maill
from lg.lg_kayit.Dao_MsSql    import  Dao_MsSql
from lg.lg_kayit.Dao_MySql    import  Dao_MySql
from lg.lg_kayit.Dao_SqLite    import  Dao_SqLite
from lg.lg_kayit.Dao_Txt import Dao_Txt

#Veritabani Dosyalari
import sqlite3
conn = None
curs = None
#
_IConn = None
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
    

def myConnection():
    try:
        return sqlite3.connect(SURUCU + OBS_DOSYA)
    except:
        return None
def myFConnection():
    try:
        return sqlite3.connect(SURUCU + OBS_FIHRIST_DOSYA)
    except:
        return None
    
def obs_dosya_olustur():
    conn =myConnection() #if None
    curs = conn.cursor()
    sql = "CREATE TABLE GIDEN_RAPOR (ID    INTEGER PRIMARY KEY AUTOINCREMENT,USER_NAME    CHAR(20) NOT NULL,TARIH    DATE, \
             KONU    CHAR(50),RAPOR    CHAR(50),ALICI    CHAR(50),ACIKLAMA CHAR(100),GONDEREN CHAR(50)); " 
    curs.execute(sql)
    sql = "CREATE TABLE E_MAIL_BILGILERI (USER_NAME    CHAR(20) NOT NULL,HESAP    CHAR(40),HOST    CHAR(30),PORT    CHAR(20), \
            SIFR    BLOB,SSL    INTEGER,TSL    INTEGER,GON_MAIL CHAR (40),GON_ISIM CHAR(50) ,PRIMARY KEY(\"USER_NAME\")); " 
    curs.execute(sql)
    sql = "CREATE TABLE IP (IPID     INTEGER PRIMARY KEY AUTOINCREMENT ,IP    CHAR(50) NOT NULL,USER_NAME    CHAR(20) ); "
    curs.execute(sql)
    sql = "CREATE TABLE USER_DETAILS (CDID INTEGER PRIMARY KEY AUTOINCREMENT ,USER_PROG_KODU    CHAR(10) NOT NULL,USER_NAME    \
            CHAR(20),USER_SERVER CHAR(50), USER_PWD_SERVER BLOB,USER_INSTANCE_OBS CHAR(50),USER_IP_OBS CHAR(50),USER_PROG_OBS CHAR(20), \
            DIZIN CHAR(200),YER CHAR(1), DIZIN_CINS CHAR(1),IZINLI_MI CHAR(1),CALISAN_MI CHAR(1),HANGI_SQL CHAR(10),LOG INTEGER , LOG_YERI CHAR(75)); " 
    curs.execute(sql)
    sql = "CREATE TABLE EKSTRE (TARIH CHAR(10) ,EVRAK INTEGER,IZAHAT CHAR(100),KOD CHAR(10),KUR DOUBLE, BORC DOUBLE,ALACAK DOUBLE ,BAKIYE DOUBLE) ;"  
    curs.execute(sql)
    sql = "CREATE TABLE USERS (USER_NAME    CHAR(20),USER_PWD BLOB,USER_LEVEL CHAR(2),USER_DB_IZIN CHAR(255),USER_MAIL CHAR(50),USER_YENI_DOSYA_ACMA INTEGER, \
            USER_YENI_DOSYA_ACMA_SERVER INTEGER, PRIMARY KEY(\"USER_NAME\")); " 
    curs.execute(sql)
    sql = "CREATE TABLE LOG_MAIL (USER_NAME    CHAR(20),E_MAIL     CHAR(50), AKTIV  INTEGER); " 
    curs.execute(sql)
    conn.commit()
def obs_fih_dosya_olustur():
    try:
        conn = myFConnection() #if None
        curs = conn.cursor()
        sql = "CREATE TABLE USER_DETAILS (CDID INTEGER PRIMARY KEY AUTOINCREMENT ,USER_PROG_KODU    CHAR(10) NOT NULL,    \
                USER_SERVER CHAR(50), USER_PWD_SERVER BLOB,USER_INSTANCE_OBS CHAR(50),USER_IP_OBS CHAR(50),USER_PROG_OBS CHAR(20), \
                DIZIN CHAR(200),YER CHAR(1), DIZIN_CINS CHAR(1),IZINLI_MI CHAR(1),CALISAN_MI CHAR(1),HANGI_SQL CHAR(10),LOG INTEGER , LOG_YERI CHAR(75)); " 
        curs.execute(sql)
        sql = "CREATE TABLE LOG_MAIL (USER_NAME    CHAR(20),E_MAIL     CHAR(50), AKTIV  INTEGER); " 
        curs.execute(sql)
        conn.commit()
    except Exception as e:
    # Just print(e) is cleaner and more likely what you want,
    # but if you insist on printing message specifically whenever possible...
        if hasattr(e, 'message'):
            print(e.message)
        else:
            print(e)
def surucu_kontrol():
    import os
    isExist = os.path.exists(SURUCU)
    if isExist == False:
            os.mkdir(SURUCU) 
    isExist = os.path.exists(DBYERI)
    if isExist == False:
            os.mkdir(DBYERI) 
    isExist =os.path.isfile(SURUCU + OBS_DOSYA)
    if isExist:
        propisExist =os.path.isfile(SURUCU +  "/admin.properties")
        if propisExist == False:
            #set_ilk() #obs_set_olustur();
            print("prop yok")
    else:
        obs_dosya_olustur
        #Tema_Cari.dosya_yap();
        #set_ilk()  //obs_set_olustur();
def fih_surucu_kontrol():
    import os
    isExist = os.path.exists(SURUCU)
    if isExist == False:
            os.mkdir(SURUCU) 
    isExist = os.path.exists(DBYERI)
    if isExist == False:
            os.mkdir(DBYERI) 
    isExist =os.path.isfile(SURUCU + OBS_FIHRIST_DOSYA)
    if not isExist:
        print("dos yok")
        obs_fih_dosya_olustur()
        #Tema_Cari.dosya_yap();
        #set_ilk()  //obs_set_olustur();

def char_degis (degisken):
        return degisken.replace(":","_");
            
    # do something

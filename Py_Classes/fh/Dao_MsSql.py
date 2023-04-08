'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt
import Cal_Dizini.Baglan as cdzn
from User_Islemleri.User_Details import user_detail 
import Cal_Dizini.Baglan_Log as bAGLAN_LOG
import lg.lg_kayit as lgkyt
from Global import Global  as glb
import pypyodbc 
import sqlite3
conn = ""
class Ms_Sql(IFihristt):
    def baglan(self,mesaj):
        global conn
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=' + cdzn.fihDizin.cONN_STR )
    def fih__sifirdan_L(self,user_detail ):
       
        instt = "\\" + user_detail.USER_INSTANCE_OBS
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';UID='+ user_detail.USER_SERVER+';PWD=' + user_detail.USER_PWD_SERVER +';Trust_Connection =True',
                      autocommit=True) 
        VERITABANI = "OK_Fih" + user_detail.USER_PROG_KODU
        sql = "CREATE DATABASE [" + VERITABANI + "]"
        curs = conn.cursor()
        curs.execute(sql)
        curs.commit()
        #============================
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';database='+ VERITABANI  + ';Trust_Connection =True;UID='+ user_detail.USER_SERVER+';PWD=' + user_detail.USER_PWD_SERVER) 
        sql = "CREATE TABLE Fihrist( ID int identity(1,1) CONSTRAINT PKeyid PRIMARY KEY ,Adi nvarchar(50) , Fax nvarchar(25),Tel_1 nvarchar(25),Tel_2 nvarchar(25), \
                    Tel_3 nvarchar(25),Tel_4 nvarchar(25),Ozel nvarchar(50),Mail nvarchar(50) )"
        curs = conn.cursor()
        curs.execute(sql)
        curs.commit()
        #**************************** LOG DOSYASI
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';UID='+ user_detail.USER_SERVER+';PWD=' + user_detail.USER_PWD_SERVER +';Trust_Connection =True',
                      autocommit=True) 
        VERITABANI = "OK_Fih" + user_detail.USER_PROG_KODU + "_L"
        sql = "CREATE DATABASE [" + VERITABANI + "]"
        curs = conn.cursor()
        curs.execute(sql)
        curs.commit()
        
        #****************************************
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=localhost' + instt + ';database='+ VERITABANI  + ';Trust_Connection =True;UID='+ user_detail.USER_SERVER+';PWD=' + user_detail.USER_PWD_SERVER) 

        sql = 'CREATE TABLE [dbo].[LOGLAMA](  \
                    [TARIH] [datetime] NOT NULL, \
                    [MESAJ] [nchar](100) NOT NULL,\
                    [EVRAK] [nchar](15) NOT NULL,\
                    [USER_NAME] [nchar](15) NULL \
                 ) ON [PRIMARY];'
        curs = conn.cursor()
        curs.execute(sql)
        curs.commit()
        sql = 'CREATE NONCLUSTERED INDEX [IX_LOGLAMA] ON [dbo].[LOGLAMA](    [TARIH] ASC,    [EVRAK] ASC , [USER_NAME] ASC  \
                 )WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) '
        curs = conn.cursor()
        curs.execute(sql)
        curs.commit()   
        #****************************************
        conn.commit()
        conn.close()
        # VERITABANI DOSYASI ILK ACILIS
        vtlgkayit =  lgkyt.Dao_MsSql.Dao_MsSql()
        vtlgkayit.logla("Dosya Olusturuldu" ,"", bAGLAN_LOG.fihLogDizin)
        vtlgkayit.logla("Firma Adi:" + user_detail.FIRMA_ADI ,"", bAGLAN_LOG.fihLogDizin)
        
        #*************************************** SQLITE LOG DOSYASI OLUSTUR
        VERITABANI = "OK_Fih" + user_detail.USER_PROG_KODU
        if glb.dos_kontrol(glb.LOG_SURUCU + VERITABANI + "_mSSQL"+  ".DB") == False :
            dsy = glb.LOG_SURUCU + VERITABANI + "_mSSQL"+ ".DB" ;
            conn =  sqlite3.connect(dsy)
            curs = conn.cursor()
            glb.create_table_log(dsy,user_detail.FIRMA_ADI,bAGLAN_LOG.fihLogDizin)
        #*************************************** TEXT DOSYASI ILK ACILIS
        txlgkayit =  lgkyt.Dao_Txt.Dao_Txt()
        txlgkayit.logla("Dosya Olusturuldu" ,"", bAGLAN_LOG.fihLogDizin)
        txlgkayit.logla("Firma Adi:" + user_detail.FIRMA_ADI ,"", bAGLAN_LOG.fihLogDizin)
        
        
    def fih__sifirdan_S(self,mesaj):
        pass
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mssql Database...')
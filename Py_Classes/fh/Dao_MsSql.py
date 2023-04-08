'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt
import Cal_Dizini.Baglan as cdzn
from User_Islemleri.User_Details import user_detail 
import pypyodbc 
conn = ""
class Ms_Sql(IFihristt):
    def baglan(self,mesaj):
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
        conn.commit()
        conn.close()
    def fih__sifirdan_S(self,mesaj):
        pass
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mssql Database...')
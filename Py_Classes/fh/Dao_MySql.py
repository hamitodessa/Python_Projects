'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt
#from User_Islemleri.User_Details import user_detail 


class My_Sql(IFihristt):
    def baglan(self,mesaj):
        print('Connecting to Mysql Database...' + mesaj)
    def fih__sifirdan_L(self,user_detail):
        print('Connecting to Mysql Dosya Olustur Lokal Database...' + user_detail.USER_PROG_KODU)
    def fih__sifirdan_S(self,mesaj):
        pass
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mysql Database...')
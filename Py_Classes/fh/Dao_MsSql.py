'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt
import Cal_Dizini.Baglan as cdzn
import pypyodbc 
conn = ""
class Ms_Sql(IFihristt):
    def baglan(self,mesaj):
        conn = pypyodbc.connect(r'DRIVER={SQL SERVER};Server=' + cdzn.fihDizin.cONN_STR )
    def fih__sifirdan_L(self,mesaj):
        pass
    def fih__sifirdan_S(self,mesaj):
        pass
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mssql Database...')
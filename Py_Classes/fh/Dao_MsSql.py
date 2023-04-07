'''
Created on Apr 1, 2023

@author: hamit
'''

from fh.IFihrist import IFihristt
import Cal_Dizini.Baglan as cdzn
import pypyodbc 
conn = ""
class Ms_Sql(IFihristt):
    def connect(self,mesaj):
            print(r'DRIVER={SQL SERVER};Server=' + cdzn.fihDizin.cONN_STR + ';Trust_Connection =True')
            conn = pypyodbc.connect('DRIVER={SQL SERVER};Server=' + cdzn.fihDizin.cONN_STR + ';Trust_Connection =True')
           
    def db_kontrol_L(self):
        print('Connecting to Mssql Database...')
    def disconnect(self):
        print('Disconnecting to Mssql Database...')
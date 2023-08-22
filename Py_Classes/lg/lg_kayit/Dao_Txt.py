'''
Created on Apr 1, 2023

@author: hamit
'''

from lg.lg_kayit.ILog_Kayit import ILogKayitInterface
from Global import Global  as glb
import datetime

class Dao_Txt(ILogKayitInterface):
    def logla(self,mesaj, evrak, DIZIN_BILGILERI):
        file = open(glb.LOG_SURUCU  + DIZIN_BILGILERI.mODULADI  + ".txt", "a") 
        
        file.write(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S") +  "\t" + mesaj.replace("\t", "") +  "\t" + evrak +"\t"+ glb.KULL_ADI + "\n" )    
        
        
    def log_rapor(self):
        print('Connecting to Txt Database...')
    
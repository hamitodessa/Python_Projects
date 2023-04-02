'''
Created on Apr 2, 2023

@author: hamit
'''

from Cal_Dizini.Dizin_Bilgileri import DIZIN_BILGILERI 
import Global.Global as glb
#Veritabani Dosyalari
conn = None
curs = None

class Bilgi_Oku:
    
    def bILGI_OKU(self,uSER,pROG ,  DIZIN_BILGILERI  , dOSYA_BASLANGIC):
        conn = glb.myConnection()
        
        sql = "SELECT * FROM USER_DETAILS WHERE USER_PROG_OBS='" +pROG + "' AND USER_NAME='" + uSER +"' And CALISAN_MI = 'E'"
        curs = conn.cursor()
        curs.execute(sql)
      
        result=curs.fetchall()
        print (len(curs.fetchall()))
       
        if len(curs.fetchall()) = 0:
            dIZIN = DIZIN_BILGILERI
            dIZIN.kOD = result.row["USER_PROG_KODU"]
            dIZIN.sERVER =  result.row["USER_IP_OBS"]
            dIZIN.kULLANICI = result.row["USER_SERVER"] 
            dIZIN.sIFRESI = result.row["USER_PWD_SERVER"]
            dIZIN.yER = result.row["YER"]
            dIZIN.iNSTANCE = result.row["USER_INSTANCE_OBS"]
            dIZIN.dIZIN_CINS = result.row["DIZIN_CINS"]
            dIZIN.dIZIN = result.row["DIZIN"]
            dIZIN.hAN_SQL = result.row["HANGI_SQL"]
            dIZIN.cDID= result.row["CDID"]
            dIZIN.lOG =result.row["LOG"]
            dIZIN.lOGLAMA_YERI = result.row["LOG_YERI"]
            print(dIZIN.sIFRESI)
            conn.commit()

'''
Created on Apr 2, 2023

@author: hamit
'''


import Global.Global as glb
import Yardimci_Classlar.Encrypt_Decrypt_String as sIFRELE

class Bilgi_Oku:
    
    def bILGI_OKU(self,uSER,pROG ,  DIZIN_BILGILERI  , dOSYA_BASLANGIC):
        conn = glb.myFConnection()
        sql = "SELECT * FROM USER_DETAILS WHERE USER_PROG_OBS='" + pROG + "' AND USER_NAME='" + uSER +"' And CALISAN_MI = 'E'"
        curs = conn.cursor()
        curs.execute(sql) 
        result = curs.fetchall()
        if len(result) > 0:
            for row in result:
                dIZIN = DIZIN_BILGILERI
                dIZIN.kOD = row[1]
                dIZIN.sERVER =  row[6]
                dIZIN.kULLANICI = row[3] 
                dIZIN.sIFRESI = sIFRELE.dCRYPT(row[4])
                dIZIN.yER = row[9]
                dIZIN.iNSTANCE = row[5]
                dIZIN.dIZIN_CINS = row[10]
                dIZIN.dIZIN = row[8]
                dIZIN.hAN_SQL = row[13]
                dIZIN.cDID= row[0]
                dIZIN.lOG = row[14]
                dIZIN.lOGLAMA_YERI = row[15]
            if dIZIN.yER == "L" :
                if dIZIN.hAN_SQL =="MS SQL" :
                    port = dIZIN.sERVER 
                    if  not port == "":
                        port =  ":" + port 
                    dIZIN.cONN_STR =  "localhost "+ port +";instanceName=" + dIZIN.iNSTANCE + " ; database=" + dOSYA_BASLANGIC  + dIZIN.kOD 
                elif dIZIN.hAN_SQL == "MY SQL" : 
                    dIZIN.cONN_STR =  "localhost:" + dIZIN.sERVER + "/" + dOSYA_BASLANGIC  + dIZIN.kOD 
            else:
                if dIZIN.hAN_SQL == "MS SQL" :
                    dIZIN.cONN_STR = dIZIN.sERVER + ";instanceName=" +dIZIN.iNSTANCE + " ; database=" +  dOSYA_BASLANGIC +dIZIN.kOD 
                elif dIZIN.hAN_SQL == "MY SQL" :
                    dIZIN.cONN_STR = dIZIN.sERVER + " /" +  dOSYA_BASLANGIC +dIZIN.kOD 
        conn.commit()

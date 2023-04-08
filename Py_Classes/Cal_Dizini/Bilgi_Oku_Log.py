'''
Created on Apr 2, 2023

@author: hamit
'''

import Global.Global as glb

class Bilgi_Oku_Log:
    def bILGI_OKU(self, dIZIN  , dOSYA_BASLANGIC, oDIZIN ):
        if (oDIZIN.yER == "L") :
            if (oDIZIN.hAN_SQL == "Ms Sql"):
                dIZIN.kULLANICI = oDIZIN.kULLANICI
                dIZIN.sIFRESI = oDIZIN.sIFRESI
                port = "" 
                if (oDIZIN.sERVER != "") :
                    port =  ":" + oDIZIN.sERVER
                dIZIN.cONN_STR =  "localhost" + port + ";instanceName=" + oDIZIN.iNSTANCE + " ; database=" + dOSYA_BASLANGIC  + oDIZIN.kOD + "_LOG"
                dIZIN.mODUL =    dOSYA_BASLANGIC  + oDIZIN.kOD + "_mSSQL" + ".DB" #//SQLITE
                dIZIN.mODULADI =    dOSYA_BASLANGIC  + oDIZIN.kOD  + "_mSSQL" #//TEXT DOSYA
            elif (oDIZIN.hAN_SQL == "My Sql") :
                dIZIN.kULLANICI = oDIZIN.kULLANICI
                dIZIN.sIFRESI = oDIZIN.sIFRESI
                dIZIN.cONN_STR =  "localhost/" + dOSYA_BASLANGIC  + oDIZIN.kOD + "_log" #;//VERITABANI
                dIZIN.mODUL =    dOSYA_BASLANGIC  + oDIZIN.kOD + "_mYSQL" + ".DB" #//SQLITE
                dIZIN.mODULADI =  dOSYA_BASLANGIC  + oDIZIN.kOD + "_mYSQL" #//TEXT DOSYA
        else:
            if (oDIZIN.hAN_SQL == "Ms Sql") :
                dIZIN.kULLANICI = oDIZIN.kULLANICI
                dIZIN.sIFRESI = oDIZIN.sIFRESI
                dIZIN.cONN_STR = oDIZIN.sERVER + ";instanceName=" + oDIZIN.iNSTANCE + " ; database=" +  dOSYA_BASLANGIC + oDIZIN.kOD + "_LOG" #//VERITABANI
                dIZIN.mODUL =   glb.char_degis( oDIZIN.sERVER) +  dOSYA_BASLANGIC  + oDIZIN.kOD + "_mSSQL" + ".DB" #//SQLITE
                dIZIN.mODULADI =  glb.char_degis( oDIZIN.sERVER) +  dOSYA_BASLANGIC  + oDIZIN.kOD  + "_mSSQL" #//TEXT DOSYA
            elif (oDIZIN.hAN_SQL == "My Sql") :
                dIZIN.kULLANICI = oDIZIN.kULLANICI
                dIZIN.sIFRESI = oDIZIN.sIFRESI
                dIZIN.cONN_STR =  oDIZIN.sERVER + "/" +  dOSYA_BASLANGIC + oDIZIN.kOD + "_log" #//VERITABANI
                dIZIN.mODUL =   glb.char_degis( oDIZIN.sERVER) +  dOSYA_BASLANGIC  + oDIZIN.kOD + "_mYSQL" + ".DB" #//SQLITE
                dIZIN.mODULADI =   glb.char_degis( oDIZIN.sERVER) + dOSYA_BASLANGIC  + oDIZIN.kOD + "_mYSQL"  #//TEXT DOSYA
            
      
            
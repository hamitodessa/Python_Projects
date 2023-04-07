'''
Created on Apr 7, 2023

@author: hamit
'''

import sqlite3
from Global import Global  as glb
from User_Islemleri.User_Details import user_detail 
def calisanmi_degis( user , program ):
    conn =  sqlite3.connect(glb.SURUCU + glb.OBS_FIHRIST_DOSYA)
    curs = conn.cursor()
    curs.execute("UPDATE  USER_DETAILS  SET CALISAN_MI='' WHERE USER_NAME ='" + user + "'  AND USER_PROG_OBS='"+ program +"'")
    conn.commit()
    conn.close()
def details_yaz(user_detail):
    conn =  sqlite3.connect(glb.SURUCU + glb.OBS_FIHRIST_DOSYA)
    curs = conn.cursor()
    curs.execute("DELETE FROM USER_DETAILS WHERE CDID = '" + user_detail.CDID + "'" )
    conn.commit()
    curs.execute('INSERT INTO USER_DETAILS (USER_PROG_KODU,USER_NAME,USER_SERVER,USER_PWD_SERVER,USER_INSTANCE_OBS,USER_IP_OBS, \
                USER_PROG_OBS,DIZIN,YER,DIZIN_CINS,IZINLI_MI,CALISAN_MI,HANGI_SQL,LOG,LOG_YERI) \
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)' ,(user_detail.USER_PROG_KODU,user_detail.USER_NAME,user_detail.USER_SERVER,user_detail.USER_PWD_SERVER 
                                                          ,user_detail.USER_INSTANCE_OBS,user_detail.USER_IP_OBS,user_detail.USER_PROG_OBS,user_detail.DIZIN ,
                                                          user_detail.YER,user_detail.DIZIN_CINS,user_detail.IZINLI_MI,user_detail.CALISAN_MI,user_detail.HANGI_SQL,
                                                          user_detail.LOG,user_detail.LOG_YERI))
    conn.commit()
    conn.close()
    
 

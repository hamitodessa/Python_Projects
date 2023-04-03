'''
Created on Apr 2, 2023

@author: hamit
'''

from Cal_Dizini.Dizin_Bilgileri import DIZIN_BILGILERI
from Cal_Dizini.Bilgi_Oku_Log import Bilgi_Oku_Log
import Cal_Dizini.Baglan as BAGLAN 

    
kurLogDizin = DIZIN_BILGILERI()  # // Kur
fihLogDizin = DIZIN_BILGILERI()  # // Fihrist
cariLogDizin = DIZIN_BILGILERI() # // Cari
fatLogDizin = DIZIN_BILGILERI()  # // Fatura
adrLogDizin = DIZIN_BILGILERI()  # // Adres
gunLogDizin = DIZIN_BILGILERI()  # // Gunluk
kamLogDizin = DIZIN_BILGILERI()  # // Kambiyo
smsLogDizin = DIZIN_BILGILERI()  # // SMS
fihLogDizin = DIZIN_BILGILERI()  # // Fihrist
    
    
def cONNECT():
    b_OKU = Bilgi_Oku_Log()
    b_OKU.bILGI_OKU(cariLogDizin,"OK_Car", BAGLAN.cariDizin);
    b_OKU.bILGI_OKU(kurLogDizin,"OK_Kur", BAGLAN.kurDizin);
    b_OKU.bILGI_OKU(fatLogDizin,"OK_Fat", BAGLAN.fatDizin);
    b_OKU.bILGI_OKU(adrLogDizin,"OK_Adr", BAGLAN.adrDizin);
    b_OKU.bILGI_OKU(gunLogDizin,"OK_Gun", BAGLAN.gunDizin);
    b_OKU.bILGI_OKU(kamLogDizin,"OK_Kam", BAGLAN.kamDizin);
    b_OKU.bILGI_OKU(smsLogDizin,"OK_Sms", BAGLAN.smsDizin);
    b_OKU.bILGI_OKU(fihLogDizin,"OK_Fih", BAGLAN.fihDizin);
   

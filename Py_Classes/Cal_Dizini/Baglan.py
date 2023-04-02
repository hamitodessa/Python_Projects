'''
Created on Apr 2, 2023

@author: hamit
'''

from Cal_Dizini.Dizin_Bilgileri import DIZIN_BILGILERI
from Cal_Dizini.Bilgi_Okuma import Bilgi_Oku


    
kurConn = None 
cariConn = None 
fatConn = None 
adrConn = None 
gunConn = None 
kamConn = None 
smsConn = None 
fihConn = None 

    
    
kurDizin = DIZIN_BILGILERI()  # // Kur
fihDizin = DIZIN_BILGILERI()  # // Fihrist
cariDizin = DIZIN_BILGILERI() # // Cari
fatDizin = DIZIN_BILGILERI()  # // Fatura
adrDizin = DIZIN_BILGILERI()  # // Adres
gunDizin = DIZIN_BILGILERI()  # // Gunluk
kamDizin = DIZIN_BILGILERI()  # // Kambiyo
smsDizin = DIZIN_BILGILERI()  # // SMS
fihDizin = DIZIN_BILGILERI()  # // Fihrist
    
    
def cONNECT(uSER):
    b_OKU = Bilgi_Oku();
    b_OKU.bILGI_OKU(uSER, "Kur", kurDizin,"OK_Kur")
    b_OKU.bILGI_OKU(uSER, "Cari Hesap",cariDizin,"OK_Car");
    b_OKU.bILGI_OKU(uSER, "Fatura",fatDizin,"OK_Fat");
    b_OKU.bILGI_OKU(uSER, "Adres",adrDizin,"OK_Adr");
    b_OKU.bILGI_OKU(uSER, "Gunluk",gunDizin,"OK_Gun");
    b_OKU.bILGI_OKU(uSER, "Kambiyo",kamDizin,"OK_Kam");
    b_OKU.bILGI_OKU(uSER, "Fihrist",fihDizin,"OK_Fih");
    b_OKU.bILGI_OKU(uSER, "Sms",smsDizin,"OK_Sms");
    
cONNECT("hamit")
print(kurDizin.kOD)
print(cariDizin.kOD)
    
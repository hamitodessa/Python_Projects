'''
Created on Apr 3, 2023

@author: hamit
'''
from cryptography.fernet import Fernet
def eNCRYPT(kelime):
    key = b'YH765E2kt-Y3FDIB3VkySCV0FODSJFR_VH_jnlboNqQ=' #Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(kelime.encode())
    return encMessage
def dCRYPT(kelime):
    key = b'YH765E2kt-Y3FDIB3VkySCV0FODSJFR_VH_jnlboNqQ=' #Fernet.generate_key()
    fernet = Fernet(key)
    decMessage = fernet.decrypt(kelime).decode()
    return decMessage

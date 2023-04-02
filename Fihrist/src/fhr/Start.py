'''
Created on Apr 1, 2023

@author: hamit
'''

from Global import Global  as glb

from fh.Access_DB import Fihrist_Access 

fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)

fih.baglan("Deneme mesaji")

'''
Created on Apr 1, 2023

@author: hamit
'''

from Global import Global  as glb

from fh.Access_DB import Fihrist_Access 


glb._Fihrist = glb.Ms_Sql
glb._IFihrist_Loger = [glb.Maill,glb.Dao_MsSql,glb.Dao_MySql,glb.Dao_SqLite,glb.Dao_Txt]


fih = Fihrist_Access(glb._Fihrist,glb._IFihrist_Loger)

fih.baglan("Deneme mesaji")

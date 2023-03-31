'''
Created on Mar 30, 2023

@author: hamit
'''
from comtypes.client import CreateObject

access = CreateObject('Access.Application')

from comtypes.gen import Access

DBEngine = access.DBEngine
db = DBEngine.CreateDatabase('C:\\OBS_SISTEM\\test.mdb', Access.DB_LANG_GENERAL)
      # For me, test.mdb was created in my My Documents folder when I ran the script 

db.BeginTrans()

db.Execute("CREATE TABLE test (ID Text, numapples Integer)")
db.Execute("INSERT INTO test VALUES ('ABC', 3)")

db.CommitTrans()
db.Close()

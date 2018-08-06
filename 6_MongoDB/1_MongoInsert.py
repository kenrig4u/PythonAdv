# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:17:37 2018

@author: SilverDoe
"""
# pip install pymongo
# importing module
from pymongo import MongoClient
 
# creation of MongoClient
client=MongoClient()
 
# Connect with the portnumber and host
client = MongoClient('localhost', 27017) # or client = MongoClient('mongodb://localhost:27017/')
 
# Access database
mydatabase = client['details'] # or mydatabase = client.details
serverStatusResult=mydatabase.command("serverStatus")
print(serverStatusResult)

# inserting a record ==========================================================
'''
Collections and databases are created when the first document is inserted into them
'''
rec={
'name': 'Tom', 
'likes': ['breaking rules', 'cheating', 'magic'], 
'remark': 'bad',
'health':30
}
 

result = mydatabase.students.insert_one(rec)
print(result.acknowledged)
print(result.inserted_id)

# inserting many records ======================================================

rec1={
'name': 'Arun', 
'likes': ['quoting', 'pcs', 'nature'], 
'remark': 'okay',
'health':50
}

rec2={
'name': 'Gominyo', 
'likes': ['quoting', 'pcs', 'nature'], 
'remark': 'good',
'health':70
}

rec3={
'name': 'Inuyasha', 
'likes': ['quoting', 'pcs', 'nature'], 
'remark': 'good',
'health':100
}

results = mydatabase.students.insert_many([rec1,rec2,rec3])
print(results.acknowledged)
print(results.inserted_ids)



result = mydatabase.students.create_index( [{ "rank": 1 }] )
print(result.acknowledged)
















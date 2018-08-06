# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:51:17 2018

@author: SilverDoe
"""

# pip install pymongo
# importing module
from pymongo import MongoClient
 
# creation of MongoClient
client=MongoClient()
 
# Connect with the port number and host
client = MongoClient('localhost', 27017) # or client = MongoClient('mongodb://localhost:27017/')
 
# Access database
mydatabase = client['details'] # or mydatabase = client.details
serverStatusResult=mydatabase.command("serverStatus")
#print(serverStatusResult)

# get the count of records/documents===========================================

count = mydatabase.students.count()
print(count)


# get the count of records/documents that matche a name =======================

count = mydatabase.students.find({'name':'Tom'}).count()
print(count)


# select a record==============================================================

record = mydatabase.students.find_one()
print(record)

# select a record that matches the object id ==================================
from bson.objectid import ObjectId
record = mydatabase.students.find_one({'_id':ObjectId("5b19569413fa6519f0bf72ba")})
print(record)

# select a record where name = Tom ============================================

record = mydatabase.students.find_one({'name':'Tom'})
print(record)

# select all records===========================================================

cursor = mydatabase.students.find()
for record in cursor: # cursor.sort("name") to sort on the basis of the name
    print(record)

# select all records where name = Tom =========================================
cursor = mydatabase.students.find({'name':'Tom'})
for record in cursor:
    print(record)
    
    
# select all records where health less than 50 ================================
    
cursor = mydatabase.students.find({"health": {"$lt":50}})
for record in cursor:
    print(record)   
    

# select all records where health greater than 50 =============================
    
cursor = mydatabase.students.find({"health": {"$gt":50}})
for record in cursor:
    print(record)   
    
    
# select all records where name equals either "Arun" or "Tom"==================   
    '''
    Although you can express this query using the $or operator, 
    use the $in operator rather than the $or operator when performing
    equality checks on the same field
    '''
    
cursor = mydatabase.students.find({'name':{'$in':['Tom','Arun']}}) 
for record in cursor:
    print(record)    
    
    
# select all records where name = Gominyo or remark = good ====================
    
cursor = mydatabase.students.find({"$or":[{'name':'Arun'},{'remark':'good'}]})
for record in cursor:
    print(record)   

    
# select all records where remark = good and name = Tom =======================
    
cursor = mydatabase.students.find({"name": "Gominyo", "remark": 'good'})
for record in cursor:
    print(record)


# select all records where remark = good and either health less than 100 or name starts with I=======================
    
cursor = mydatabase.students.find({'remark':'good','$or':[{'health':{'$lt':100}},{'name':{'$regex':'^I'}}]})
for record in cursor:
    print(record)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
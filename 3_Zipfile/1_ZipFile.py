# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:57:28 2018

@author: SilverDoe
"""


from zipfile import ZipFile
 
file_name = r"E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest.docx"
 
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()
    xml_content = zip.read('word/document.xml')
    print(xml_content)
 
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
    
    
f = 'test1.zip'
z = zipfile.ZipFile(f, "r")
zinfo = z.namelist()
for name in zinfo:
    with z.open(name) as f1:
        fi1 = f1.readlines()
for line in fi1:
print(line)
    
    
    
import os
import zipfile
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
zipf = zipfile.ZipFile('Zipped_file.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('./my_folder', zipf)
zipf.close()
    
    


import csv, io, zipfile

zip_file    = zipfile.ZipFile("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\protest.docx",'r')
items_file  = zip_file.open("word/document.xml", 'r')
# items_file.readable = lambda: True
# items_file.writable = lambda: False
# items_file.seekable = lambda: False
# items_file.read1 = items_file.read
items_file  = io.TextIOWrapper(items_file,encoding='utf-8', newline='')
print(items_file)



for idx, row in enumerate(csv.DictReader(items_file)):
    print('Processing row {0} -- row = {1}'.format(idx, row))
    
    
    

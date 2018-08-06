# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:13:24 2018

@author: SilverDoe
"""

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO,BytesIO
    
    

import time

begin = time.time()
buffer = b""
for i in range(0, 50000):
    buffer += b"Hello World"
end = time.time()
seconds = end - begin
print("Concat:", seconds)

begin = time.time()
buffer = BytesIO()
for i in range(0, 50000):
    buffer.write(b"Hello World")
end = time.time()
seconds = end - begin
print("BytesIO:", seconds)


# writing to file
f = open("E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\byteio.txt","wb")
f.write(buffer.getvalue())
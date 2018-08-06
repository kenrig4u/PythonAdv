# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 22:53:54 2018

@author: SilverDoe
"""

# ======================= match() =============================================
import re
print(re.match('center','centre'))

print(re.match('...\w\we','centre'))


#======================== search() ============================================
import re
match=re.search('aa?yushi','ayushi')
match.group()


match=re.search('aa?yushi?','ayush ayushi')
match.group()

match=re.search('\w*end','Hey! What are your plans for the weekend?')
match.group()

match=re.search('i\sS','Ayushi Sharma')
match.group()

match=re.search('\w+c{2}\w*','Occam\'s Razor')
match.group()

match=re.search(r'[\w.-]+@[\w-]+.[\w]+','Please mail it to ayushiwashere@gmail.com')
match.group()

#================ search() group extraction ===================================

match=re.search(r'([\w.-]+)@([\w-]+).([\w]+)','Please mail it to ayushiwashere@gmail.com')
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))

# ============= findall() with files ==========================================

import os
import re
os.chdir('E:\\')
f=open('trashcode\\www.txt')

match=re.findall(r'java[\w]*',f.read()) #matches the words starting with java
for i in match:
    print(i)
    
    
# ============= findall() with groups =========================================
import re    
match=re.findall(r'([\w]+)\s([\w]+)','Harry Potter, Hermione Granger, Ron Weasley')
for i in match:
    print(i)
    
#============== findall() greedy ==============================================
    
match=re.findall(r'(<.*>)','<em>Strong</em> <i>Italic</i>')
for i in match:
    print(i)
    
#============== findall() non-greedy ==========================================
    
match=re.findall(r'(<.*?>)','<em>Strong</em> <i>Italic</i>')
for i in match:
    print(i)

#==============================================================================
match=re.findall(r'</?\w+>','<em>Strong</em> <i>Italic</i>')
for i in match:
    print(i)
    
    
#==============================================================================
    
match=re.findall('(a*?)b','aaabbc')
for i in match:
    print(i)
    
#=============== Substitution =================================================

nword = re.sub('^a','an','a apple')
print(nword)
    
    
    
#=============== Match words separated by Hyphens =============================    


text = "how-do-you-do"
match = re.findall(r'\w+(?:-\w+)+',text)
for i in match:
    print(i)
    
    
    
    
match=re.search(r'([\w]+)@([\w]+).([\w]+)','Please mail it to ayu-shiw-ashere@gmail.com')
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.group(3))





















   
    
    
    
    
    
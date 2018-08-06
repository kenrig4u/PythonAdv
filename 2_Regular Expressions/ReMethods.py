# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 15:22:04 2018

@author: SilverDoe
"""

'''
>>The search scans the string start to end.
>>The whole pattern must match, but not necessarily the whole string.
>>The search stops at the first match.
>>Python findall() returns a list of all matches found.

# Methods ===========================

match(pattern,string,flag=0)
search(pattern,string,flag=0)
findall(pattern,string,option)
sub(pattern, repl, string, max=0)


# Optional flags for match() and search() ====================

re.I    Performs case-insensitive matching.

re.L    Interprets words according to the current locale. This interpretation 
        affects the alphabetic group (\w and \W), as well as word boundary behavior(\b and \B).
        
re.M    Makes $ match the end of a line (not just the end of the string) and 
        makes ^ match the start of any line (not just the start of the string).
        
re.S    Makes a period (dot) match any character, including a newline.

	
re.U    Interprets letters according to the Unicode character set. This flag 
        affects the behavior of \w, \W, \b, \B.
        
re.X    Permits "cuter" regular expression syntax. It ignores whitespace (except
        inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.

# Optional flags for findall() ====================

re.IGNORECASE   This Python Regular Expression ignore case ignores the case while matching.
re.MULTILINE    Working with a string of multiple lines, this allows ^ and $ to match the 
                start and end of each line, not just the whole string
                
re.DOTALL       .* does not scan everything in a multiline string; it only matches
                 the first line. This is because . does not match a newline. To
                 allow this, we use DOTALL.
                                                                          

# R prefix ==========================

>>> '\n'
'\n'

>>> r'\n'
'\\n'

>>> print('\n')


>>> print(r'\n')
\n

>>> '\s'
'\s'

>>> r'\s'
'\\s'

>>> print('\s')
\s

>>> print(r'\s')
\s

In a raw string backslash characters are treated literally instead of signifying 
special treatment of the following character. Unless an 'r' or 'R' prefix is present,
 escape sequences in strings are interpreted according to rules similar to those 
 used by Standard C. The recognized escape sequences are:
     
Escape Sequence   Meaning Notes
\newline  Ignored  
\\    Backslash (\)    
\'    Single quote (')     
\"    Double quote (")     
\a    ASCII Bell (BEL)     
\b    ASCII Backspace (BS)     
\f    ASCII Formfeed (FF)  
\n    ASCII Linefeed (LF)  
\N{name}  Character named name in the Unicode database (Unicode only)  
\r    ASCII Carriage Return (CR)   
\t    ASCII Horizontal Tab (TAB)   
\uxxxx    Character with 16-bit hex value xxxx (Unicode only) 
\Uxxxxxxxx    Character with 32-bit hex value xxxxxxxx (Unicode only) 
\v    ASCII Vertical Tab (VT)  
\ooo  Character with octal value ooo
\xhh  Character with hex value hh



'''


#==================== Match and Group =========================================

import re

line = "I have built a sand castle"

mobj = re.match( r'(.*) a (.*?) .*', line, re.M|re.I)

if mobj:
   print("mobj.group() : ", mobj.group())
   print("mobj.group(1) : ", mobj.group(1))
   print("mobj.group(2) : ", mobj.group(2)) 
   print("mobj.groups() : ", mobj.groups())
else:
   print("No match!!")
   
   
#================== Search function ===========================================
 
import re

line = "I have built a sand castle"

mobj = re.search( r'(.*) a (.*?) .*', line, re.M|re.I)

if mobj:
   print("mobj.group() : ", mobj.group())
   print("mobj.group(1) : ", mobj.group(1))
   print("mobj.group(2) : ", mobj.group(2)) 
   print("mobj.groups() : ", mobj.groups())
else:
   print("No match!!")   
   
   
#============= Match vs Searching =============================================
   
'''
Python offers two different primitive operations based on regular expressions: 
match checks for a match only at the beginning of the string, while search
checks for a match anywhere in the string 
'''

import re

#match
line = "I have built a sand castle"

mobj = re.match( r'castle', line, re.M|re.I)
if mobj:
   print("match --> mobj.group() : ", mobj.group())
else:
   print("match -->No match!!")

#search
sobj = re.search( r'castle', line, re.M|re.I)
if sobj:
   print("search --> searchObj.group() : ", sobj.group())
else:
   print("search -->Nothing found!!")
   
   
#================== Search and replace ========================================
   
'''
This method replaces all occurrences of the RE pattern in string with repl, substituting
all occurrences unless max provided. This method returns modified string
'''

import re

phone = "8943-008-651 # This is my Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print("Phone Num : ", num)


num = re.sub(r'\bis\b', "is not", phone)    
print("Phone Num : ", num)
   
   




#================ FindAll =====================================================


match=re.findall(r'reason','''If there is a reason why the universe exists, 
                 then there should be a reason behind the cause of its existence as well''')
for i in match:
    print(i)
    
    


















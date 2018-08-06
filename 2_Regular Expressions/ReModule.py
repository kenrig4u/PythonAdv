# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 21:13:05 2018

@author: SilverDoe
"""

#================== Regular Expressions =======================================

'''
>> A regular expression in Python is a sequence of characters, that defines a search pattern.

>> This pattern can be used in a string-searching algorithm to “find” or “find and replace” on strings.

>> To use regex in python, you need to "import re" module.

'''


#================= Metacharacters =============================================

'''

^        Matches the start of the string

.        Matches a single character, except a newline
          But when used inside square brackets, a dot is matched
    
[ ]      	A bracket expression matches a single character from the ones inside it
         [abc] matches ‘a’, ‘b’, and ‘c’
         [a-z] matches characters from ‘a’ to ‘z’
         [a-cx-z] matches ‘a’, ’b’, ’c’, ’x’, ’y’, and ‘z’
         
[^ ]     [^abc] matches all characters except ‘a’, ‘b’ and ‘c’

( )      Parentheses define a marked subexpression, also called a block, or a capturing group
         
{m,n}    Matches the preceding character minimum m times, and maximum n times

{m}	      Matches the preceding character exactly m times

{m,}     Matches m or more occurrences of preceding expression 

?	      Matches the preceding character zero or one times
         ab?c matches ‘ac’ or ‘abc’
         
*       	Matches the preceding character zero or more times
         ab*c matches ‘ac’, ‘abc’, ‘abbc’, and so on
         [ab]* matches ‘’, ‘a’, ‘b’, ‘ab’, ‘ba’, ‘aba’, and so on
         (ab)* matches ‘’, ‘ab’, ‘abab’, ‘ababab’, and so on
         
+        	Matches the preceding character one or more times
         ab+c matches ‘abc’, ‘abbc’, ‘abbbc’, and so on, but not ‘ac’
         
|        The choice operator matches either the expression before it, or the one after
         abc|def matches ‘abc’ or ‘def
         
\w       Matches a word character (a-zA-Z0-9)
\W       matches single non-word characters
        
\b	     Matches the boundary between word and non-word characters

\s      Matches a single whitespace character
\S      matches a single non-whitespace character
    
\d      Matches a single decimal digit character (0-9)
\D      Matches nondigits.

\A      Matches beginning of string.

\z      Matches end of string.
\Z      Matches end of string. If a newline exists, it matches just before newline.

\G      Matches point where last match finished.

\b      Matches word boundaries when outside brackets. Matches backspace (0x08) when inside brackets
\B      Matches nonword boundaries.

\t, \n, \r, \f  Tab, newline, return, form feed

\1...\9 Matches nth grouped subexpression

	
\10     Matches nth grouped subexpression if it matched already. Otherwise refers to the octal representation of a character code.

[ \t\r\n\f] Match a whitespace character


\       A single backslash inhibits a character’s specialness
        When unsure if a character has a special meaning, put a \ before it
        + ? . * ^ $ ( ) [ ] { } | \ You can escape a control character by preceding it with a backslash

$	     A dollar matches the end of the string


'''

#================== Regex examples ============================================

'''
	
python      Match "python"

====== Character Classes =============

[Pp]ython   Match "Python" or "python"

rub[ye]     Match "ruby" or "rube"

[aeiou]     Match any one lowercase vowel
	
[0-9]       Match any digit; same as [0123456789]

[a-z]       Match any lowercase ASCII letter

	
[A-Z]       Match any uppercase ASCII letter

[a-zA-Z0-9] Match any of the above

	
[^aeiou]    Match anything other than a lowercase vowel

[^0-9]      Match anything other than a digit


====== Special Character Classes =======

.           Match any character except newline

\d          Match a digit: [0-9]

\D          Match a nondigit: [^0-9]

\s          Match a whitespace character: [ \t\r\n\f]

\S          Match nonwhitespace: [^ \t\r\n\f]

\w          Match a single word character: [A-Za-z0-9_]

\W          Match a nonword character: [^A-Za-z0-9_]


======= Repetition Cases ===============

	
ruby?       Match "rub" or "ruby": the y is optional

ruby*       Match "rub" plus 0 or more ys

ruby+       Match "rub" plus 1 or more ys
	
\d{3}       Match exactly 3 digits

\d{3,}      Match 3 or more digits

\d{3,5}     Match 3, 4, or 5 digits


======= Nongreedy Repetition ============

<.*>    Greedy repetition: matches "<python>perl>"

<.*?>   Nongreedy: matches "<python>" in "<python>perl>"

======= Grouping with Parantheses =======

\D\d+               No group: + repeats \d

(\D\d)+             Grouped: + repeats \D\d pair

([Pp]ython(, )?)+   Match "Python", "Python, python, python", etc.

([Pp])ython&\1ails  Match python&pails or Python&Pails

(['"])[^\1]*\1      Single or double-quoted string. \1 matches whatever the 1st
                     group matched. \2 matches whatever the 2nd group matched, etc.
                     
 
======== Alternatives ===================

python|perl         Match "python" or "perl"    

rub(y|le))          Match "ruby" or "ruble"

Python(!+|\?)       "Python" followed by one or more ! or one ?


======= Anchors =========================

^Python             Match "Python" at the start of a string or internal line

Python$             Match "Python" at the end of a string or line

\APython            Match "Python" at the start of a string

Python\Z            Match "Python" at the end of a string

\bPython\b          Match "Python" at a word boundary

\brub\B             \B is nonword boundary: match "rub" in "rube" and "ruby" but not alone

Python(?=!)         Match "Python", if followed by an exclamation point.

Python(?!!)         Match "Python", if not followed by an exclamation point.


======= Special Syntax with Parentheses ====

R(?#comment)        Matches "R". All the rest is a comment

R(?i)uby            Case-insensitive while matching "uby"

R(?i:uby)           Same as above

rub(?:y|le))        Group only without creating \1 backreference

'''

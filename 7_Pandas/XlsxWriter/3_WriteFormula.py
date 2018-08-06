# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 01:59:13 2018

@author: SilverDoe
"""

'''

write_formula(row, col, formula[, cell_format[, value]])

row     : (int) – The cell row (zero indexed).

col     : (int) – The cell column (zero indexed).

formula : (string) – Formula to write to cell.

cell_format : (Format) – Optional Format object.

value   : Optional result. The value if the formula was calculated.


https://xlsxwriter.readthedocs.io/worksheet.html
'''

import pandas as pd

df = pd.read_excel('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\formulafile.xlsx', sheet_name='Sheet1')
print (df)

writer = pd.ExcelWriter('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\formulafile1.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1',index = False)

worksheet = writer.sheets['Sheet1']
worksheet.write_string(0, 6, 'Total')
# write_number(row, col, number)

for i in range(1,len(df)+1):
    worksheet.write_formula(i, 6, '=SUM(A'+str(i+1)+':F'+str(i+1)+')')
    
writer.save()

'''

worksheet.write_formula(0, 0, '=B3 + B4')
worksheet.write_formula(1, 0, '=SIN(PI()/4)')
worksheet.write_formula(2, 0, '=SUM(B1:B5)')
worksheet.write_formula('A4', '=IF(A3>1,"Yes", "No")') #Both row-column and A1 style notation are supported
worksheet.write_formula('A5', '=AVERAGE(1, 2, 3, 4)')
worksheet.write_formula('A6', '=DATEVALUE("1-Jan-2013")')

worksheet.write_array_formula(0, 0, 2, 0, '{=TREND(C1:C3,B1:B3)}')
worksheet.write_array_formula('A1:A3',    '{=TREND(C1:C3,B1:B3)}')

write_blank(row, col, blank[, cell_format])

Excel 2010 and 2013 added functions which weren’t defined in the original file specification.
These functions are referred to as future functions. Examples of these functions are ACOT, 
CHISQ.DIST.RT , CONFIDENCE.NORM, STDEV.P, STDEV.S and WORKDAY.INTL. In XlsxWriter these
require a prefix:

worksheet.write_formula('A1', '=_xlfn.STDEV.S(B1:B10)')

'''



























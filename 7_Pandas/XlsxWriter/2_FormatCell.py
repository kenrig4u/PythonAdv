# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 01:44:41 2018

@author: SilverDoe
"""

#========================= format cell color ==================================
import pandas as pd
df = pd.DataFrame({'Pass/Fail':['Pass','Fail','Fail'],'expect':[1,2,3]})
print (df)

writer = pd.ExcelWriter('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\savefile.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

workbook  = writer.book
red_format = workbook.add_format({'bg_color':'red'})
green_format = workbook.add_format({'bg_color':'green'})

worksheet = writer.sheets['Sheet1']
worksheet.conditional_format('B2:B4', {'type': 'text',
                                      'criteria': 'containing',
                                       'value':     'Fail',
                                       'format': red_format})

worksheet.conditional_format('B2:B4', {'type': 'text',
                                      'criteria': 'containing',
                                       'value':   'Pass',
                                       'format':  green_format})
writer.save()



#=========================== Dynamic cell formatting ==========================
import string
import pandas as pd
df = pd.DataFrame({'Pass/Fail':['Pass','Fail','Fail'],'expect':[1,2,3]})
print (df)

writer = pd.ExcelWriter('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\savefile1.xlsx', engine='xlsxwriter')

df.to_excel(writer, sheet_name='Sheet1')

workbook  = writer.book
red_format = workbook.add_format({'bg_color':'red','bold': True, 'italic': True})
green_format = workbook.add_format({'bg_color':'green'})


#dict for map excel header, first A is index, so omit it
d = dict(zip(range(25), list(string.ascii_uppercase)[1:]))
print (d)

#set column for formatting
col = 'Pass/Fail'
excel_header = str(d[df.columns.get_loc(col)])
#get length of df
len_df = str(len(df.index) + 1)
rng = excel_header + '2:' + excel_header + len_df
print (rng)

worksheet = writer.sheets['Sheet1']
worksheet.conditional_format(rng, {'type': 'text',
                                      'criteria': 'containing',
                                       'value':     'Fail',
                                       'format': red_format})

worksheet.conditional_format(rng, {'type': 'text',
                                      'criteria': 'containing',
                                       'value':   'Pass',
                                       'format':  green_format})
writer.save()
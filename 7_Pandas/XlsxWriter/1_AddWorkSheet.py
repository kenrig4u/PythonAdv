# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 00:53:26 2018

@author: SilverDoe
"""

'''

The worksheet class represents an Excel worksheet. It handles operations such as writing
data to cells or formatting worksheet layout.

A worksheet object isn’t instantiated directly. Instead a new worksheet is created by 
calling the add_worksheet() method from a Workbook() object.

https://xlsxwriter.readthedocs.io/workbook.html

https://xlsxwriter.readthedocs.io/worksheet.html

'''
import xlsxwriter

workbook   = xlsxwriter.Workbook('E:\\Documents\\PythonProjects\\1_Basics\\DataForFiles\\xlsxfile1.xlsx')

worksheet1 = workbook.add_worksheet() # adding a new sheet
worksheet2 = workbook.add_worksheet() # adding another one

worksheet1.write('A1', 123)

workbook.close()
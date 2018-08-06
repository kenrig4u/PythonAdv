# 2) Read excel,Open excel, get sheets from workbook, getting sheets from the sheets
# getting rows and columns from the sheets

from pyexcel_xls import save_data, read_data

data = {"sheet 1":[[1,2,3],[4,5,6]], "sheet 2":[[2,3,'Arun'],['python','data']]}
save_data('E:\\trashcode\\aasd.xlsx',data)

rdata = read_data('E:\\trashcode\\aasd.xlsx')
print(rdata)


import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet() 
worksheet.write('A2','Test data')
workbook.close()
import os
import glob
import csv
import xlwt 

for csvfile in glob.glob(os.path.join('.', '*.csv')):
    wb = xlwt.Workbook()
    ws = wb.add_sheet('data')
    with open(csvfile, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, val in enumerate(row):
                ws.write(r, c, val)
    wb.save(csvfile + '.xls') 
 


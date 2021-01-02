"""Read Excel File"""
import xlrd
data = xlrd.open_workbook('E:/tempdata/kldata.xlsx')

# Get Sheet names from the excel file
data.sheet_names()
# Get count of rows and columns from each sheet
for i in data.sheet_names():
    print("Rows in", i , data.sheet_by_name(i).nrows)
    print("Columns in", i, data.sheet_by_name(i).nrows)


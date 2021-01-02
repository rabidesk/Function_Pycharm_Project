# Read Excel File as whole

import pandas as pd
data = pd.ExcelFile('E:/tempdata/kldata.xlsx')
# Get Sheet names from the excel file
data.sheet_names

# Get count of rows and columns from each sheet
df1 = pd.read_excel(data,sheet_name="Sheet1") # read 1st sheet
print(df1.shape)
df2 = pd.read_excel(data,sheet_name="Sheet2") # read 2nd sheet
print(df2.shape)
# Read individual sheet
import pandas as pd

# Get count of rows and columns from each sheet
df1 = pd.read_excel('E:/tempdata/kldata.xlsx', sheet_name = "Sheet1")
print(df1.shape)



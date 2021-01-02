"""Import Excel sheet as csv and xlsx in python
"""
# import csv
import pandas as pd

data = pd.read_excel('kldata.xlsx') # when read xlsx type of file

data = pd.read_csv('Workbook2.csv')  # When read csv type of file

print(data.head()) # head() function only can read first 5 rows from datasheet


# Note if No matching distribution found for 2.0 or required to install for above version then
# pip install openpyxl to solve this issue.
# In some case required to install numpy up to data version with numpy and pandas
# pip install numpy == 1.19.3
# pip install pandas
"""Read Excel File"""
import pylightxl as xl # Install pylightlx package
data = xl.readxl(fn='E:/tempdata/kldata.xlsx') # Use suitable attribute if not find

# Get Sheet names from the excel file
data.ws_names
# Get count of rows and columns from each sheet
for i in data.ws_names:
    print("Rows in", i , len(data.ws(ws=i).col(col=1)))
    print("Columns in", i , len(data.ws(ws=i).row(row=1)))

import pandas as pd
file = pd.ExcelFile("sales.xlsx")
print(file.sheet_names)
sheet = file.parse('sales')
print(sheet)
print(type(sheet))
print(sheet.Date)
print(sheet.Amount.sum())
print(sheet.loc[0])
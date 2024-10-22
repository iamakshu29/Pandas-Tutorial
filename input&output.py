import pandas as pd

url = "https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv"
names = pd.read_csv(url)
print(names)


"""
Export a DataFrame to a .csv file
1. "to_csv" method exports a dataframe to csv file
2. first args is file name
3. By Default, pandas will include the index. Set the index parameter to False to exclude the Index
4. The "columns" parameter limits the exported columns.

"""

names.to_csv("baby_names.csv",index=False,columns=["Year of Birth","Gender","Child's First Name"])



"""
Import Excel File into Pandas

1. the read_excel function reads an Excel file into a DataFrame
2. Use the sheet_name parameter if the workbook contains multiple worksheets. Pass a single worksheet name or list of worksheet names/index positions.
3. Pass the sheet_name parameter arguement of None to include all worksheets.
4. Pandas will store multiple worksheets in a Python dictionary. The keys will be the worksheet names, and the values will be the DataFrames.
5. None means capture all

"""
excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Single Worksheet.xlsx")
# print(excel)


# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name="Data 1")
# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name=0)
# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name="Data 2")
# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name=1)
# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name=["Data 1","Data 2"])
# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name=[0,1])
# multi_excel = pd.read_excel("C:/Users/verma/Downloads/pandas/pandas/Complete/Data - Multiple Worksheets.xlsx",sheet_name=None)
# print(multi_excel["Data 1"])



"""
Export Excel File from Pandas

1. The ExcelWriter class writes one or more DataFrames to an excel File
2. Use a context manager (the with keyword) in combination with the ExcelWriter object and an assigned variable.
3. Invoke the to_excel method on every DataFrame to include the Excel workbook and pass in the ExcelWriter object at the first arguement.
4. The to_excel method supports sheet_name , index, and columns parameters.

"""
females = names[names["Gender"]=="FEMALE"]
males = names[names["Gender"]=="MALE"]
print(males)

    # 1 more accurate and save us from memory leak
with pd.ExcelWriter("Baby Data.xlsx") as excel_file:
    females.to_excel(excel_file,sheet_name="Females",index=False)
    males.to_excel(excel_file,sheet_name="Males",index=False,columns=["Year of Birth","Ethnicity","Rank"])

    # 2 direct approach
females.to_excel("abc.xlsx",sheet_name="Females",index=False)  


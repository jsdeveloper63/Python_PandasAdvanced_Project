import numpy as np
import pandas as pd
import statistics
df = pd.read_csv('../sales_2009data/SalesJan2009.csv', index_col=0)
#Passing index_col=0 in the argument of read_csv will make the first column as index
# We can set the index manually as well
#print(df.set_index("TitleORCOlumnNAme"))
#IF WE WANT TO USE A COLUMN NAME AS INDEX BUT REMAIN THAT INDEX AS COLUMNS AS WELL
#print(df.set_index('title', drop = False))

#CHANGING DISPLAY OPTIONS TO VISIBLY VIEW ALL ROWS AND COLUMNS
#print(df.set_option('display.max_columns'))
#print(df.set_option('display.max_coluns', 40)) (OR WHATEVER NO. of COLUMNS WE HAVE)
#print(df.set_option('display.max_columns'))

#print(df)
#type returns a fully qualified name
#print(type(df))
#print(df.dtypes)
#print(df.info())

#print(df.head(2))
#print(df.columns)
#print(df.describe())

#Difference between data series and dataframe
#A single column of data returns a series
#Series has 2 components, index and data
# Each index label holds value of data
#print(df['State'])
#print(type(df['State']))
#state = df['State']
#print(type(state))


# 3 ways to select subsets of data
#[], loc, iloc
#print(df['Country'].head(2))
#Select multiple columns using lists
#print(df[['Name','Account_Created']])
#OR WE CAN Even create a new list making the subsets selection
#cols = ['Product', 'Price', 'Payment_Type']

#print(df[cols].head(2))

#loc : has its own set of rules in selecting data
# we can simultaneously select rows and columns in lol
# It is primary selected by label
#rows = ['1/2/09 6:17', '1/12/09 21:30']
#cols = ['State', 'Account_Created', 'Last_Login']
#print(df.loc[rows, cols])

#Selecting two rows and one column returns two value series
#rows = ['1/2/09 6:17', '1/12/09 21:30']
#cols = 'State'
#print(df.loc[rows, cols])
#print(df.loc[rows])
#TO view the data from just selecting the single row index
#print(df.loc['1/2/09 6:17', :])

#Using slice notation to select a range of rows
#BAscially it selects all the columns from the table depending upon the rows range selected
#print(df.loc['1/2/09 6:17': '1/12/09 21:30',::100])

#Using iloc : Every item in rows and columns should be integer
#rows = [2, 4]
#cols = [0,-1]
#print(df.iloc[rows,cols])
#print(df.iloc[:5, cols])
#SELECT SOME ROWS AND ALL columns
#print(df.iloc[0:11, :])
#SELECT SOME ROWS AND some columns
#print(df.iloc[0:2, :])
#SELECTING single row as a data series
#print(df.iloc[1,:])
#Selecting single row as a dataFrame
#Selecting one row and all columns
#print(df.iloc[[1],:])
#print(df[100:200:10])


#Boolean Indexing
#Using isin for multiple conditioning
#countryAustralia= df['Country']== 'Australia'
#print(df[countryAustralia])
#Transaction_visa = df['Payment_Type']== 'Visa'
#print(df[Transaction_visa])
#product_required = df['Product']== 'Product1'
#AustraliancardTransaction= countryAustralia & Transaction_visa & product_required

#print(df[AustraliancardTransaction])

#country = ['Australia', 'Malta', 'Switzerland']
#filt = df['Country'].isin(country)
#print(df[filt])

#isna method checks if a value is missing in column and returns true
# or false in a Series
#filt = df['Payment_Type'].isna()
#print(df[filt])
#print(df['Payment_Type'].isna())

# query method
# quesry method does not work with columns with spaces in it
#print(df.query('Product == "Product1" and Country == "Austria"'))

#Slicing with just [], loc or iloc
#print(df[10:15])
#print(df.iloc[10:20])

#Select a single cell with at and iat
# it is similar to loc but it can only take one label
#print(df.iat[100,4])#Gives a single precise value

#using numpy array for subselection of data
#values = df.values
#print(values)
#print(%time -n 5 values[-30, 5])

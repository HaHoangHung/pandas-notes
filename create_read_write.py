import pandas as pd

# Creating data:
# There are two core objects in pandas: DataFrame and Series

# DataFrame: a table which contains an array of individual entries, each of which has a certain value
# Each entry corresponds to a row (a record) and a column

df_i = pd.DataFrame({"Yes" : [50, 21], "No" : [13, 36]})
print(df_i)

df_s =pd.DataFrame({"Halbert" : ["That's cool.", "This is arkward."], "Cory" : ["You're weird.", "It's weird."]})
print(df_s)

# In default, row labels will be ascending count (0, 1, 2,...), we can assign values to it using an 'index' parameter

df_si =pd.DataFrame({"Halbert" : ["That's cool.", "This is arkward."], "Cory" : ["You're weird.", "It's weird."]},
                    index=["Catch Phrase 1", "Catch Phrase 2"])
print(df_si)

# Series: a sequence of data values; if a DataFrame is a table, a Series is a list

sr = pd.Series([1, 2, 3, 4, 5])
print(sr)

# Apart from 'index' parameter, a Series does not have a column name, it only has one overall name

sr_i = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(sr_i)


# Reading data files:
# Data can be stored in any of a number of different forms and formats
# By far the most basic of these is the humble CSV (Comma-Seperated Values) file 

wine_reviews = pd.read_csv(r"C:\Users\Triple.H\Desktop\Python\Panda_Course\Data Files\winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.shape) 
print(wine_reviews.head()) #grab the first five rows

# We can save a DataFrame to a CSV file:
# sr_i.to_csv("file_name")
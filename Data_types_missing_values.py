import pandas as pd
reviews = pd.read_csv(r"C:\Users\Triple.H\Desktop\Python\Panda_Course\Data Files\winemag-data-130k-v2.csv", index_col=0)

# This lesson is about how to investigate data types within a DataFrame or Series. 
# You'll also learn how to find and replace entries.

# Dtypes:
# The data type for a column in a DataFrame or a Series is known as dtype
# You can use dtype property to get the type of a specific column
reviews.price.dtype
# Alternatively, the dtypes property returns the dtype of every column in the DataFrame:
reviews.dtypes
# One peculiarity to keep in mind is that columns consisting entirely of strings are instead given the object type.
# WARNINNG: The statement above refers to the older versions of pandas, beware of that
# It's possible to convert a column of one type into another wherever such a conversion makes sense
reviews.points.astype('float64')
# A DataFrame or Series index has its own dtype, too:
reviews.index.dtype


# Missing data:
# Entries missing values are given the value NaN, short for "Not a Number". 
# For technical reasons these NaN values are always of the float64 dtype.
# To select NaN entries you can use pd.isnull() (or its companion pd.notnull()).
reviews[pd.isnull(reviews.country)]
# Replacing missing values is a common operation. Pandas provides a really handy method for this problem: fillna(). 
# fillna() provides a few different strategies for mitigating such data.
# For example, we can simply replace each NaN with an "Unknown":
reviews.region_2.fillna('Unknown')
# Or we could fill each missing value with the first non-null value that appears sometime after the given record in the database. 
# This is known as the backfill strategy.

# Alternatively, we may have a non-null value that we would like to replace.
# One way to reflect this in the dataset is using the replace() method:
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")
# the replace() method is worth mentioning here because it's handy for replacing missing data 
# which is given some kind of sentinel value in the dataset: things like "Unknown", "Undisclosed", "Invalid", and so on.


reviews = reviews.dropna()  # return the same DataFrame but without None cells

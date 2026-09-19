import pandas as pd
import pprint
reviews = pd.read_csv(r"C:\Users\Triple.H\Desktop\Python\Panda_Course\Data Files\winemag-data-130k-v2.csv", index_col=0)
# Now you'll learn how to use pandas functions to change the names of the offending entries to something better.
# You'll also explore how to combine data from multiple DataFrames and/or Series

# Renaming:
# The first function we'll introduce here is rename(), which lets you change index names and/or column names.
reviews.rename(columns={'points' : 'score'})
# rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively.
# It supports a variety of input formats, but usually a Python dictionary is the most convenient.
# Here is an example using it to rename some elements of the index.
reviews.rename(index={0 : 'firstEntry', 1 : 'secondEntry'})
# Both the row index and the column index can have their own name attribute. 
# The complimentary rename_axis() method may be used to change these names.
reviews.rename_axis('wine', axis='rows').rename_axis('fields', axis='columns')


# Combining:
# Pandas has three core methods for combining different DataFrames and/or Series
# In order of increasing complexity: concat(), join(), merge()
# Most of what merge() can do can also be done more simply with join()

# The simplest combining method is concat(). 
# Given a list of elements, this function will smush those elements together along an axis.
# This is useful when we have data in different DataFrame or Series objects but having the same fields (columns).
canadian_youtube = pd.read_csv(r"Panda_Course/Data Files/CAvideos.csv", index_col=0)
british_youtube = pd.read_csv(r"Panda_Course/Data Files/GBvideos.csv", index_col=0)
pd.concat([canadian_youtube, british_youtube])

# join() lets you combine different DataFrame objects which have an index in common.
left = canadian_youtube.set_index(['trending_date'])
right = british_youtube.set_index(['trending_date'])
left.join(right, lsuffix='__CAN', rsuffix='__UK')
# The lsuffix and rsuffix parameters are necessary here 
# because the data has the same column names in both British and Canadian datasets.
# If this wasn't true (because, say, we'd renamed them beforehand) we wouldn't need them.



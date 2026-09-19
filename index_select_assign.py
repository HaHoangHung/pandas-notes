import pandas as pd
# Native accessors:
# Native Python objects provide good ways of indexing data.
# Pandas carries all of these over, which helps make it easy to start with.

reviews = pd.read_csv(r"C:\Users\Triple.H\Desktop\Python\Panda_Course\Data Files\winemag-data-130k-v2.csv", index_col=0)

# In Python, we can access data from DataFrame in two ways:
# Same as an object: attributes
reviews.country
# Same as an dict: keys
reviews['country']
# To drill down to a single specific value, we need only use the indexing operator [] once more
reviews['country'][0]


# Indexing in pandas:
# Pandas has its own accessor operators, loc and iloc. 
# For more advanced operations, these are the ones you're supposed to be using.
# Both loc and iloc are row-first, column-second.

# Index_based selection (iloc):
reviews.iloc[0]          # retrieve first row
reviews.iloc[:, 0]       # retrieve first column
reviews.iloc[:3, 0]      # retrieve first column of the first, second and third row
reviews.iloc[1:3, 0]     # retrieve first column of only the first and second row
reviews.iloc[[1, 2, 3], 0]
reviews.iloc[-5:]        # retrieve last five rows

# Label_based selection (loc):
reviews.loc[:, 'country']    #retrieve country column
# Since your dataset usually has meaningful indices, it's usually easier to do things using loc instead
reviews.loc[:, ["country", "points"]]

# iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. 
# So 0:10 will select entries 0,...,9. 
# loc,meanwhile, indexes inclusively. 
# So 0:10 will select entries 0,...,10.


# Maniulating the index:
# We can manipulate the index in any way we see fit.
reviews.set_index("title")
# This is useful if you can come up with an index for the dataset which is better than the current one.


# Conditional selection:
# We often need to ask questions based on conditions
reviews.country == "Italy"  # produce a series of True/False base on the country of each record
# This result can then be used inside of loc to select the relevant data:
reviews.loc[reviews.country == "Italy"]
# We can also use the ampersand (&) or the pipe (|) for more logically specification
reviews.loc[(reviews.country == "Italy") & (reviews.points >= 90)]

# Pandas comes with a few built-in conditional selectors, two of which we will highlight here.
# The first is 'isin': lets you select data whose value "is in" a list of values
reviews.loc[reviews.country.isin(["Italy", "France"])]
# The second is isnull (and its companion notnull): let you highlight values which are (or are not) empty (NaN)
reviews.loc[reviews.price.notnull()]


# Assigning data:
# Assigning data to a DataFrame is easy. You can assign either a constant value:
reviews["critic"] = "everyone"
reviews["critic"]
# Or with an iterable of values:
reviews["index_backwards"] = range(len(reviews), 0, -1)
reviews["index_backwards"]

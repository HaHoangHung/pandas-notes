import pandas as pd
# Often we want to group our data, and then do something specific to the group the data is in.
reviews = pd.read_csv(r"C:\Users\Triple.H\Desktop\Python\Panda_Course\Data Files\winemag-data-130k-v2.csv", index_col=0)

# Groupwise analysis:
# One function we've been using heavily thus far is the value_counts() function. 
# We can replicate what value_counts() does by doing the following:
reviews.groupby('points').points.count()    # reviews.points.value_count()
# The DataFrame.groupby() method is used to split-apply-combine
reviews.groupby('points').price.min()   # return a series
# Each group we generate as being a slice of our DataFrame containing only data with values that match.
# This DataFrame is accessible to us directly using the apply() method
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])   # the name of the first wine reviewed from each winery
# For even more fine-grained control, you can also group by more than one column
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# Another groupby() method worth mentioning is agg(), 
# which lets you run a bunch of different functions on your DataFrame simultaneously.
reviews.groupby(['country']).price.agg(['count', min, max])


# Multi-indexes:
# Depending on the operation we run, groupby() will sometimes result in what is called a multi-index.
# A multi-index differs from a regular index in that it has multiple levels.
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
mi = countries_reviewed.index   # example for multi-indexes, in this case, list of corresponding country and province pairs
# Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices.
# However, in general the multi-index method you will use most often is the one for converting back to a regular index
countries_reviewed.reset_index()


# Sorting:
# When outputting the result of a groupby, the order of the rows is dependent on the values in the index, not in the data.
# To get data in the order we want it in, we can sort it ourselves.
countries_reviewed.sort_values(by='len')    # should use reset_index() beforehand
# sort_values() defaults to an ascending sort, where the lowest values go first.
# However, most of the time we want a descending sort, where the higher numbers go first.
countries_reviewed.sort_values(by='len', ascending=False)

# To sort by index values, use the companion method sort_index()
countries_reviewed.sort_index()

# Finally, know that you can sort by more than one column at a time:
countries_reviewed.sort_values(by=['country', 'len'])


# Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer. 
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
# Use the describe() method to see a summary of the range of values.
reviewer_mean_ratings.describe()

# Create a Series whose index is a MultiIndexof {country, variety} pairs.
# Sort the values in the Series in descending order based on wine count.
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
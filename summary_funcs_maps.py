import pandas as pd
# Plucking the right data out of our data representation is critical to getting work done.
# However, the data does not always come out of memory in the format we want it in right out of the bat. 
# Sometimes we have to do some more work ourselves to reformat it for the task at hand.
reviews = pd.read_csv(r"C:\Users\Triple.H\Desktop\Python\Panda_Course\Data Files\winemag-data-130k-v2.csv", index_col=0)

# Summary funcions:
reviews.points.describe()   # numerical data
reviews.description.describe()   #string data

# If you want to get some particular simple summary statistic about a column in a DataFrame or a Series,
# there is usually a helpful pandas function that makes it happen.
reviews.points.mean()    # return the mean
reviews.iloc[:, 6].unique()  # return unique values
reviews.country.value_counts()   # return freq of values


# Maps:
# In data science we often have a need for creating new representations from existing data,
# or for transforming data from the format it is in now to the format that we want it to be in later.
# There are two mapping methods that you will use often.

# map():
reviews_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - reviews_points_mean)
# The function you pass to map() should expect a single value from the Series,
# and return a transformed version of that value.

# apply():
# is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
def remean_points(row):
    row.points = row.points - reviews_points_mean

print(reviews.apply(remean_points, axis='columns'))

# Note that map() and apply() return new, transformed Series and DataFrames, respectively. 
# They don't modify the original data they're called on.

# Pandas provides many common mapping operations as built-ins. 
# For example, here's a faster way of remeaning our points column:
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean
# In this code we are performing an operation between a lot of values on the left-hand side and a single value on the right-hand side.
# Pandas will also understand what to do if we perform these operations between Series of equal length.
reviews.country + " - " + reviews.region_1
# These operators are faster than map() or apply() because they use speed ups built into pandas
# However, they are not as flexible as map() or apply()

# def points_to_price(row):
#     row.points = row.points / row.price
#     return row
# temp = reviews.loc[(reviews.points.notnull() & reviews.price.notnull())]
# pp_reviews = temp.apply(points_to_price, axis='columns')
# highest_ratio = max(pp_reviews.points)
# bargain_wine = (pp_reviews.loc[pp_reviews.points==highest_ratio]).iloc[0].title
# print(bargain_wine)
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

# fruity = 0
# tropical = 0
# def count_appearance(row):
#     global fruity
#     global tropical
#     if('fruity' in row.description):
#         fruity += 1
#     if('tropical' in row.description):
#         tropical += 1
#     return row
# reviews.apply(count_appearance, axis='columns')
# descriptor_counts = pd.Series([tropical, fruity], index=["tropical", "fruity"])
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])


# Test Suite for hw1 functions
# Includes reading of example adult information dataframe

# REPL run script: exec(open('hw1Test.py').read())

# Taken from assignment sheet
import pandas as pd
# names for csv data
names =  ["age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country", "income"]
# read data straight from uci repository
adult_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data",
    header=None, names=names, sep=",\s+", na_values="?",
    verbose=True, engine='python')
test_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.test",
    header=None, names=names, sep=",\s+", na_values="?", verbose=True,
    skiprows=[0], engine='python')

# in the test set, there is an extra . at the end of income, we can remove it like this:
test_df["income"] = test_df["income"].apply(lambda x: x[:-1])

print('Columns Information:')
print(adult_df.info())
print('')
print('Summary statistics of Train dataset:')
print(adult_df.describe())
print('')
print('Summary statistics of Test dataset:')
print(test_df.describe())


### Data access ###
# Access age of first record
adult_df.at[0, 'age']
# select a subset of rows
adult_df[0:4]
# access specific columns
adult_df[['age', 'workclass']]
adult_df.age
# get numpy array for a column
adult_df.age.values
# specific rows and columns
adult_df[1:4][['age', 'workclass']]

### Data Queries ###
# Get rows where workclass is missing
adult_df[pd.isna(adult_df.workclass)].head(5)
# get records with age 18 then count how many there are
adult_df[adult_df.age == 18].count()
# group by
adult_df.groupby(['marital_status']).mean()
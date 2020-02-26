import pandas as pd
import numpy as np

# return number of records in df that have
# missing values for education
def q1(df):
   # filter df for nan values in education
   # shape returns size of dataframe (row is count)
   result = df[pd.isna(df.education)].shape[0]
   return result

# return number of records in df where
# age is between 40 and 60
def q2(df):
   # filter df for proper age range
   # use count function on age vector
   result = df[(df.age >= 40) & (df.age <= 60)].age.count()
   return result

# return average age of males in df
def q3(df):
   # filter df for sex to be male
   # get mean of age vector
   result = df[df.sex == 'Male'].age.mean()
   return result

# return number of females in df who
# come from England
def q4(df):
   # filter df for female sex
   # filter df for England
   # shape returns size of df (row is count)
   result = df[(df.sex == 'Female') & (df.native_country == 'England')].shape[0]
   return result

# return standard deviation of ages
# income should be above 50k and live in United-States
def q5(df):
   # filter df for country and income
   filtered = df[(df.native_country == 'United-States') & (df.income == '>50K')]
   # use standar deviation function on age vector
   result = filtered.age.std()
   return result

# return true if those in workclass a who earn >50K
# is greater than those in workclass b who earn >50K
def q6(df, a, b):
   # filter df for income
   income_filter = df[(df.income == '>50K')]
   # get count of workclass a (row is count)
   work_a = income_filter[(income_filter.workclass == a)].shape[0]
   # get a count of workclass b (row is count)
   work_b = income_filter[(income_filter.workclass == b)].shape[0]
   if work_a > work_b:
      return True
   return False

# return nuber of people who work >20 hours a week
# and earn <50K in income
def q7(df):
   # filter df for income
   # filter df for hours worked
   # shape returns size of df (row is count)
   result = df[(df.income == '<=50K') & (df.hours_per_week >= 20)].shape[0]
   return result

# returns average work hours for income >50k
# United-States, Canada, India, England, Germany
def q8(df):
   # note countries to track
   countries = ['United-States', 'Canada', 'India', 'England', 'Germany']
   # filter df by income and country
   filtered = df[(df.income == '>50K') & (df.native_country.isin(countries))]
   # get mean of work hours for each country
   results = filtered.groupby(['native_country']).hours_per_week.mean()
   # results is series object -> dict
   results = results.to_dict()
   keys = results.keys()
   # here we loop to note if any countries we want info
   # about is missing
   for country in countries:
      if country not in keys:
         results[country] = np.nan
   return results

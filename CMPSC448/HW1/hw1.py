import pandas as pd

# return number of records in df that have
# missing values for education
def q1(df):
   result = df[pd.isna(df.education)].shape[0]
   return result

# return number of records in df where
# age is between 40 and 60
def q2(df):
   result = df[(df.age >= 40) & (df.age <= 60)].age.count()
   return result

# return average age of males in df
def q3(df):
   result = df[df.sex == 'Male'].age.mean()
   if df[df.sex == 'Male'].age.count() == 0:
      return 0
   return result

# return number of females in df who
# come from England
def q4(df):
   result = df[(df.sex == 'Female') & (df.native_country == 'England')].shape[0]
   return result

# return standard deviation of ages
# income should be above 50k and live in United-States
def q5(df):
   filtered = df[(df.native_country == 'United-States') & (df.income == '>50K')]
   result = filtered.age.std()
   return result

def q6(df, a, b):
   pass

def q7(df):
   pass

def q8(df):
   pass

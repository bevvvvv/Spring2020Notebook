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
 
def q3(df):
   pass

def q4(df):
   pass

def q5(df):
   pass

def q6(df, a, b):
   pass

def q7(df):
   pass

def q8(df):
   pass

"""
CMPSC448 Machine Learning and AI Homework 6
XGBoost
Author: Joseph Sepich (jps6444)
"""
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# The options you can play around with are: hyperparameters for XGBoost and data preprocessing operations (normalizing data, dimensionality reduction, feature construction, etc).

# params
train_data = './data/train_data.csv'
test_data = './data/test_data.csv'
sub_path = './data/sepich_submission.csv'

# read data
train_df = pd.read_csv(train_data, sep=',',header=0)
train_cats = train_df.category
train_df = train_df.drop(columns=['category'])

test_df = pd.read_csv(test_data, sep=',',header=0)
keys = test_df.key

# split data
X_train, X_valid, y_train, y_valid = train_test_split(train_df, train_cats, test_size=0.2)

# train model
model = XGBClassifier(objective='multi:softprob',
                        learning_rate = 0.01, # eta
                        max_depth = 6, # max tree depth
                        subsample = 0.8, #ratio of training data to use
                        colsample_bytree = 0.5, # use less than all 93 features
                        n_estimators = 300) # num of trees
model.fit(X_train, y_train,
            early_stopping_rounds = 5, # help prevent overfit
            eval_set = [(X_train, y_train), (X_valid, y_valid)],
            eval_metric = 'mlogloss')

#print(model.evals_result())

# make prediction
preds = model.predict_proba(test_df)

pred_df = pd.DataFrame(data = preds)
pred_df['key'] = keys
pred_df = pred_df[['key', 0, 1, 2, 3, 4, 5, 6, 7, 8]]
pred_df = pred_df.rename(columns={0: 'group_01', 1: 'group_02', 2: 'group_03', 3: 'group_04', 4: 'group_05', 5: 'group_06', 6: 'group_07', 7: 'group_08', 8: 'group_09'})

# write prediction to file
pred_df.to_csv(sub_path, index=False)

# review
from matplotlib import pyplot

results = model.evals_result()
epochs = len(results['validation_0']['mlogloss'])
x_axis = range(0, epochs)
# plot log loss
fig, ax = pyplot.subplots()
ax.plot(x_axis, results['validation_0']['mlogloss'], label='Train')
ax.plot(x_axis, results['validation_1']['mlogloss'], label='Test')
ax.legend()
pyplot.ylabel('Log Loss')
pyplot.title('XGBoost Log Loss')
pyplot.show()

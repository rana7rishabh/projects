import numpy as np
import pandas as pd 
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import cross_val_score


#1. Loading the Data
housing=pd.read_csv('housing.csv')

#2. Create stratified shuffle_spilt
housing['income_cat']=pd.cut(housing['median_income'],
                                      bins=[0,1.5,3.0,4.5,6.0,np.inf],
                                      labels=[1,2,3,4,5])

split=StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing,housing['income_cat']):
    strat_train_set=housing.loc[train_index].drop('income_cat',axis=1)
    strat_test_set=housing.loc[test_index].drop('income_cat',axis=1)

# we will work on training data
housing=strat_train_set

# 3. seperate features and labels
housing_label=housing['median_house_value'].copy()
housing=housing.drop('median_house_value', axis=1)

#4. seperate numerical and categorical columns
num_attribs=housing.drop('ocean_proximity',axis=1).columns.tolist()
cat_attribs=['ocean_proximity']

#5. making the pipeline 

# for numerical columns
num_pipeline=Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# for categorical columns
cat_pipeline=Pipeline([
    ('one', OneHotEncoder(handle_unknown='ignore'))
])

#construct full pipeline
full_pipeline= ColumnTransformer([
    ('num', num_pipeline, num_attribs),
    ('cat', cat_pipeline, cat_attribs)
])

#6. trasnform the data 
housing_prepared=full_pipeline.fit_transform(housing)


#7. training the model 


#linear regression model
lin_reg=LinearRegression()
lin_reg.fit(housing_prepared, housing_label)
lin_preds=lin_reg.predict(housing_prepared)
# lin_rmse=root_mean_squared_error(housing_label,lin_preds)
# print(f'this is the root mean square error for linear regression {lin_rmse}')
lin_rmses=-cross_val_score(lin_reg, housing_prepared, housing_label,scoring="neg_root_mean_squared_error",cv=10)

print(pd.Series(lin_rmses).describe())


#decision tree model
dec_reg=DecisionTreeRegressor()
dec_reg.fit(housing_prepared, housing_label)
dec_preds=dec_reg.predict(housing_prepared)
# dec_rmse=root_mean_squared_error(housing_label,dec_preds)
dec_rmses=-cross_val_score(dec_reg, housing_prepared, housing_label,scoring="neg_root_mean_squared_error",cv=10)

print(pd.Series(dec_rmses).describe())


#random forest model
random_forest_regression=RandomForestRegressor()
random_forest_regression.fit(housing_prepared, housing_label)
random_forest_preds=random_forest_regression.predict(housing_prepared)
# random_forest_rmse=root_mean_squared_error(housing_label,random_forest_preds)
# print(f'this is the root mean square error for random forest regressor {random_forest_rmse}')
random_rmses=-cross_val_score(random_forest_regression, housing_prepared, housing_label,scoring="neg_root_mean_squared_error",cv=10)

print(pd.Series(random_rmses).describe())



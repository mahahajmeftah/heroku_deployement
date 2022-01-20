#importing 
import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#data
CarData = pd.read_csv('CAR_DETAILS.csv')


#features
X = CarData[['year', 'km_driven']]
y = CarData['selling_price']

#spliting data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

#Training model
linearModel = LinearRegression()
linearModel.fit(X, y)

#saving the model 
pickle.dump(linearModel, open('model.pkl', 'wb'))







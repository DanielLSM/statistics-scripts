import pandas as pd
from sklearn import linear_model
import statsmodels.api as sm

x1 = [
    12, 28, 100, 100, 8, 2, 100, 100, 5, 10, 70, 15, 2, 12, 50, 100, 3, 8, 100,
    18
]
x2 = [
    11, 24.7, 2.1, 1, 57, 1, 2.5, 100.5, 151.7, 45, 10.8, 3.5, 81, 1.2, 3.7,
    2.2, 20.6, 131.6, 118.4, 5.5
]

x3 = [6, 15, 30, 10, 5, 5, 15, 10, 8, 12, 13, 30, 5, 8, 7, 10, 6, 5, 20, 10]

x4 = [5, 5, 5, 5, 4, 4, 5, 5, 2, 5, 5, 5, 2, 3, 5, 5, 1, 1, 5, 3]

y = [
    50, 60, 66.7, 33.3, 12.5, 33.3, 50, 33.3, 50, 40, 75, 25, 33.3, 75, 75, 50,
    70, 33.3, 50, 33.3
]

print("X1:{}".format(len(x1)))
print("X2:{}".format(len(x2)))
print("X3:{}".format(len(x3)))
print("X4:{}".format(len(x4)))
print("Y:{}".format(len(y)))

In_Flight_Accidents = {'X1': x1, 'X2': x2, 'X3': x3, 'X4': x4, 'Y': y}

df = pd.DataFrame(In_Flight_Accidents, columns=['X1', 'X2', 'X3', 'X4', 'Y'])

X = df[[
    'X1',
    'X2',
    'X3',
    'X4',
]]  # here we have 2 variables for multiple regression. If you just want to use one variable for simple linear regression, then use X = df['Interest_Rate'] for example.Alternatively, you may add additional variables within the brackets
Y = df['Y']

# with sklearn
regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# # prediction with sklearn
# New_Interest_Rate = 2.75
# New_Unemployment_Rate = 5.3
# print('Predicted Stock Index Price: \n',
#       regr.predict([[New_Interest_Rate, New_Unemployment_Rate]]))

# with statsmodels
X = sm.add_constant(X)  # adding a constant

model = sm.OLS(Y, X).fit()
predictions = model.predict(X)

print_model = model.summary()
print(print_model)
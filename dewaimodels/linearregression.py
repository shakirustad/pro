import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv('weather.csv')
#read contents from csv
print(dataset.shape)
#show the shape ie rows vs collumns
print(dataset.describe())

#dataset.plot(x='MinTemp', y= 'MaxTemp', style = 'o')
#plot x and y and line as style provided
#we use matplotlib instance to plot
# plt.title('MinTemp vs MaxTemp')
# plt.xlabel('MinTemp')
# plt.ylabel('MaxTemp')
# we are plotting the above variables in the graph
print("ok1")
#plt.show()
#
# plt.figure(figsize=(15,10))
# plt.tight_layout()
# seabornInstance.displot(dataset['MaxTemp'])
# print("ok2")
# plt.show()

x = dataset['MinTemp'].values.reshape(-1,1)
# x = dataset['MinTemp'].values.flatten()

#reshape converts given array into desired array dimensional
y = dataset['MaxTemp'].values.reshape(-1,1)
print("ok3")
X_train, X_test, Y_train, Y_test = train_test_split(x,y, test_size=0.2, random_state=0)
#split the dataset into training and testing dataset

regressor = LinearRegression()
regressor.fit(X_train, Y_train)
#we use the linear regression instance to train our model on the data

print('Intercept: ', regressor.intercept_)


print('Coeeffecient', regressor.coef_)

y_pred = regressor.predict(X_test)
data = np.array([[22.1,16.8],[25.1,12.2]])
y_2 = data.reshape(-1,1)
# y_2 = data.flatten()
y_2_pred = regressor.predict(y_2)
print("ok 4 is here")
print(y_2_pred)
#predict output from the trained model
df = pd.DataFrame({'Actual': Y_test.flatten(), 'Predicted': y_pred.flatten()})
#.flatten() is used to convert multidimensional to one dimensional array
print(df)

# df1 = df.head(25)
# df1.plot(kind = 'bar', figsize = (16,10))
# plt.grid(which= 'major', linestyle='-', linewidth ='0.5', color= 'green')
# plt.grid(which='minor', linestyle= ':', linewidth='0.5', color = 'black')
#plt.show()

# plt.scatter(X_test, Y_test, color = 'gray')
#plots the the test data on graph
# plt.plot(X_test,y_pred, color='blue', linewidth=2)
#draw the regression line of the input and output ie from this line is where we predict
# plt.show()

# print("Mean Absolute Error:", metrics.mean_absolute_error(Y_test,y_pred))
# print("Mean Squared Error:", metrics.mean_squared_error(Y_test, y_pred))
# print("Root Mean Squared Error:", np.sqrt(metrics.mean_squared_error(Y_test,y_pred)))

for i in range(4):
    print("Wanna need some predictions")
    k = input()
    if k == 'y':
        print("enter the temp")
        data2 = float(input())
        data4 = float(input())
        data3 = np.array([[data2],[data4]])
        #data3.flatten()
        data3.reshape(-1,1)
        y_3pred = regressor.predict(data3)
        print("the possible temp is", y_3pred)
    else:
        print("hello model not working")
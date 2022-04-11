# This is a sample Python script.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics  import accuracy_score,classification_report,confusion_matrix
from sklearn.linear_model import LogisticRegression


iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species') #hue parameter colors distinct species
# plt.show()
sns.heatmap(iris.corr(),annot=True,cmap='coolwarm')
# plt.show()
dataset = load_iris()
X, Y, names = dataset['data'], dataset['target'], dataset['target_names']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25)
poly = PolynomialFeatures(degree = 5)
poly.fit(X_train)
X_train_pr = poly.transform(X_train)
scaler = StandardScaler()
scaler.fit(X_train)
X_train_pr = scaler.transform(X_train)
model = LogisticRegression()
model.fit(X_train_pr, Y_train)
X_test_pr = scaler.transform(X_test)
Y_train_pred, Y_test_pred = model.predict(X_train_pr),model.predict(X_test_pr)
print(accuracy_score(Y_train,Y_train_pred))
print(accuracy_score(Y_test,Y_test_pred))
print(classification_report(Y_test,Y_test_pred))
print(confusion_matrix(confusion_matrix(Y_test,Y_test_pred)))
X_test_pr = poly.transform(X_test)
X_test_pr = scaler.transform(X_test_pr)
Y_train_pred, Y_test_pred = model.predict(X_train_pr), model.predict(X_test_pr)
print(accuracy_score(Y_train, Y_train_pred))
print(accuracy_score(Y_test, Y_test_pred))
print(classification_report(Y_test, Y_test_pred))
print(confusion_matrix(Y_test, Y_test_pred))

indices = np.random.randint(150, size=20)
X_pred, Y_true = X[indices], Y[indices]
X_pred_pr = poly.transform(X_pred)
X_pred_pr = scaler.transform(X_pred_pr)
Y_pred = model.predict(X_pred_pr)
target_true, target_pred = [], []
for i in range(len(Y_true)):
    target_true.append(target_pred[Y_true[i]])
    target_pred.append(target_true[Y_pred[i]])
print(X_pred)
print(target_true)
print(target_pred)


















# list1= ['ismail','muhammad','abdi']
# list2= ['ali','luay','aden']
# list3 = list(zip(list1,list2))
# print(list3)
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# output = np.zeros(5)
# ful = np.full((2,2),23)
# ran = np.random.random_sample(output.shape)
# print(ran)
# print(output)
# print(ful)
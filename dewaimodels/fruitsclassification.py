import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics




fruits = pd.read_table('fruit_data.txt')
print(fruits.head())

# print(fruits.shape())
print(fruits['fruit_name'].unique())
print(fruits.groupby('fruit_name').size())
sns.countplot(fruits['fruit_name'],label = "Count")
# plt.show()
fruits.drop('fruit_label', axis=1).plot(kind='box', subplots= True, layout = (2,2), sharex =False, sharey =False, figsize= (9,9), title ='Box plot for input variable')

plt.savefig('fruits_box')
plt.show()

feature_names =['mass', 'width', 'height', 'color_score']
x = fruits[feature_names]
y =fruits['fruit_label']

from sklearn.preprocessing import MinMaxScaler
X_train, X_test, Y_train, Y_test = train_test_split(x,y, random_state=(0))
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test =scaler.fit_transform(X_test)

#logistic regression
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, Y_train)
print('Accuracy of Logistic Regression classifier on training set: {:.2f}'.format(logreg.score(X_train, Y_train)))
print('Accuracy of Logistic Regression classifier on testing set: {:.2f}'.format(logreg.score(X_test, Y_test)))

#Decision tree
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(X_train,Y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'.format(clf.score(X_train, Y_train)))
print('Accuracy of Decision Tree classifier on training set: {:.2f}'.format(clf.score(X_test, Y_test)))

#KNN classifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
print('Accuracy of Knn classifier on training set: {:.2f}'.format(knn.score(X_train, Y_train)))
print('Accuracy of Knn classifier on training set: {:.2f}'.format(knn.score(X_test, Y_test)))

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb =GaussianNB()
gnb.fit(X_train, Y_train)
print('Accuracy of Naive Bayes classifier on training set: {:.2f}'.format(gnb.score(X_train, Y_train)))
print('Accuracy of Naive Bayes classifier on training set: {:.2f}'.format(gnb.score(X_test, Y_test)))

#Support Vector Machines
from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, Y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'.format(svm.score(X_train, Y_train)))
print('Accuracy of SVM classifier on training set: {:.2f}'.format(svm.score(X_test, Y_test)))



from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
pred = clf.predict(X_test)
print(confusion_matrix(Y_test, pred))
print(classification_report(Y_test, pred))
#precision= ratio of predicted total positive observations eg 4 apples predicted out of 4 apples
# , recall= ratio of predicted total positive observations eg 4 to total number in class
# , f1-score= weighted avarage of precision and recall
# support= number of correctly predicted datapoint
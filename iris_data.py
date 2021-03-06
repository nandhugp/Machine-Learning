#Importing libraries
import numpy as np
from sklearn import preprocessing,model_selection,neighbors
import pandas as pd

#Reading the file

df=pd.read_csv('E:/Nandhu/Datasets/iris.data.txt')

# There are strings in these data, so we have to convert them into strings
df.label[df.label=="Iris-setosa"]=1
df.label[df.label=="Iris-versicolor"]=2
df.label[df.label=="Iris-virginica"]=3

#Filling values with -99999 if there are NaN values
df.fillna(value=-99999,inplace=True)



#Features
X=np.array(df.drop(['label'],1))
#Label
#Making test array for prediction
example_measures=np.array([[5,3.5,2,1.5],[7,8,9,10]])

#Since our test array doesn't have the label data we have to reshape to our array to make it work
example_measures=example_measures.reshape(2, -1)

#Our prediction
prediction=clf.predict(example_measures)


#Printing the prediction and score
print(prediction)
print(score)
y=np.array(df['label'])

#Splitting our data into training and testing data
X_train,X_test,y_train,y_test=model_selection.train_test_split(X,y,test_size=0.2)

#Calling our K nearest neighbor classifier
clf=neighbors.KNeighborsClassifier()

#Training our data
clf.fit(X_train,y_train)

#Testing the data and storing the accuracy
score=clf.score(X_test,y_test)

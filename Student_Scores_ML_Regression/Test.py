import pandas as pd 
import numpy as np
import tensorflow
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import plotly.express as px

data = pd.read_csv("C:\\Users\\ventu\\Python Projects\\Student Scores\\student-mat.csv", sep=";")

data = data[["G1","G2","G3","studytime","failures","absences","age"]]

#I want to predict the student's final score using the parameters listed above. I will be using a 90/10 train test split
predict = "G3"
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)

#Cross validation using KFolds
from sklearn.model_selection import KFold
kf = KFold(n_splits=10)

average_accuracy = 0
for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    linear.fit(x_train, y_train)
    average_accuracy += linear.score(x_test,y_test)
    print(linear.score(x_test,y_test))
print(average_accuracy/10)

#creating an interactive scatterplot chart using plotly and colors are assigned to a gradient
import plotly.graph_objects as go
sampleChart = go.Figure()

def create_trace(chartname, predictions, y_test, color):
    chartname.add_trace(go.Scatter(
        x = predictions,
        y = y_test,
        mode = 'markers',
        marker_color = color
    ))

colors = ['#00b6d6', '#00a7ce', '#0098c6', '#0088be', '#0079b6', '#006aae', '#015ba5', '#014c9d', '#013d95', '#012e8d', '#011e85', '#010f7d', '#010075']
i = 0

#loop that generates a new traces for each iteration of KFolds validation, we can see the variance between the prediction accuracy
#of the different train/test splits and prints out an average of the 10 runs
average_accuracy = 0
for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    linear.fit(x_train, y_train)
    acc = linear.score(x_test,y_test)
    average_accuracy += acc
    predictions = linear.predict(x_test)
    create_trace(sampleChart, predictions, y_test, colors[i])
    i += 1


print(average_accuracy/10)

sampleChart.update_layout(
    title = "Actual vs Predicted Scores",
    xaxis_title = "Predicted Scores",
    yaxis_title = 'Actual Scores'
)
sampleChart.show()

from IPython.display import Image
Image(filename='C:\\Users\\ventu\Python Projects\\Plot.png')

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=1000)

rfChart = go.Figure()

colors = ['#00b6d6', '#00a7ce', '#0098c6', '#0088be', '#0079b6', '#006aae', '#015ba5', '#014c9d', '#013d95', '#012e8d', '#011e85', '#010f7d', '#010075']
i = 0

#same loop as above but now we are using random forest regression instead of multivariate linear regression
average_accuracy = 0
for train_index, test_index in kf.split(x):
    x_train, x_test = x[train_index], x[test_index]
    y_train, y_test = y[train_index], y[test_index]
    rf.fit(x_train, y_train)
    acc = rf.score(x_test,y_test)
    average_accuracy += acc
    predictions = rf.predict(x_test)
    create_trace(rfChart, predictions, y_test, colors[i])
    i += 1

Image(filename='RFPlot.png')
rfChart.show()

average_accuracy/10



import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('fatherandsonheights.csv')

print df.head()
print ""
print "Training"
#Set de entrenamiento
x_train = df['fatherheight'].values[:,np.newaxis]
y_train = df['sonheight'].values

lm = LinearRegression()

#Train
lm.fit(x_train, y_train)

#Testing differents parent heigth to predict sons heigth data
x_test = [[72.8],[61.1],[67.4],[70.2],[75.6],[60.2],[65.3],[59.2]]
#x_test = [[72.8]]

predictions = lm.predict(x_test)
print "Giving the data set"
print x_test
print "The predictions are"
print predictions

#Lets plot this thing

plt.scatter(x_train, y_train,color="b")
plt.plot(x_test,predictions,color='black',linewidth=3)

plt.xlabel('father heigth')
plt.ylabel('son heigth')
plt.show()

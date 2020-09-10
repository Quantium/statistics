import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('cars.csv')

print(df.head())

x_train = df.loc[:,'buying':'safety']
y_train = df.loc[:,'class']

tree = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0);

#Entrenando el modelo
tree.fit(x_train,y_train)

#Testing
prediction = tree.predict([[4,3,2,1,2,3]])

print(prediction)

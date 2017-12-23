import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('volcanic.csv')

print df.head()

kmeans = KMeans(n_clusters=2)
kmeans = kmeans.fit(df)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

x_test = [[4.671,67],[2.885,61],[1.666,90],[5.623,54],[2.678,80],[1.875,60]]

prediction = kmeans.predict(x_test)

print prediction

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


df = pd.read_csv('volcanic.csv')
x_test = [[4.671,67],[2.885,61],[1.666,90],[5.623,54],[2.678,80],[1.875,60]]
colors = ['blue','green','yellow','red']


kmeans = KMeans(n_clusters=2)
kmeans = kmeans.fit(df)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

prediction = kmeans.predict(x_test)

print prediction

# some plots, the funny part
y = 0
for x in labels:
    plt.scatter(df.iloc[y,0],df.iloc[y,1],color=colors[x])
    y += 1

for x in range(2):
    lines = plt.plot(centroids[x,0],centroids[x,1],'kx')

plt.title('2 clusters')
plt.xlabel('eruptions time')
plt.ylabel('waiting between eruptions')
plt.show()

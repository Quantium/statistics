import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

k = 2
df = pd.read_csv('volcanic.csv')
x_test = [[4.671,67],[2.885,61],[1.666,90],[5.623,54],[2.678,80],[1.875,60]]
colors = ['blue','green','yellow','red']


kmeans = KMeans(n_clusters=k)
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

for x in range(k):
    lines = plt.plot(centroids[x,0],centroids[x,1],'kx')
    plt.setp(lines,ms=15.0)
    plt.setp(lines,mew=2.0)

plt.title(str(k)+' clusters')
plt.xlabel('eruptions time')
plt.ylabel('waiting between eruptions')
plt.show()

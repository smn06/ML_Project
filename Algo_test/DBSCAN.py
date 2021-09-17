import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN


# Importing the dataset
dataset = pd.read_csv('../Data_Set/Final/test.csv')
X = dataset.iloc[:, [2, 7]].values

clustering= DBSCAN(eps=1, min_samples=3,metric='euclidean').fit(X)

y_hc = clustering.fit_predict(X)
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 50, c = 'red', label = 'Good Characters')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 50, c = 'blue', label = 'Neutral Characters')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 50, c = 'green', label = 'Bad Characters')


plt.title('Density Based Spatial Clustering of Applications with Noise(DBCSAN)')
plt.xlabel('Character')
plt.ylabel('Power')
plt.legend()
plt.show()


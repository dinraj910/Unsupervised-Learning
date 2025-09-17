# Step 1: Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 2: Load Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)

print("Dataset shape:", X.shape)
print(X.head())

# Step 3: Apply K-Means (try with K=3, since Iris has 3 species)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# Step 4: Add cluster labels to dataset
X['Cluster'] = y_kmeans

# Step 5: Evaluate clustering
inertia = kmeans.inertia_
sil_score = silhouette_score(X.drop('Cluster', axis=1), y_kmeans)

print("Inertia (WCSS):", inertia)
print("Silhouette Score:", sil_score)

# Step 6: Visualize clusters (using first two features for 2D)
plt.figure(figsize=(8,6))
sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,1], hue=X['Cluster'], palette="Set2")
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 
            s=200, c='red', marker='X', label='Centroids')
plt.title("K-Means Clustering on Iris Dataset")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Step 1: Try multiple K values
inertia = []
sil_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    y_pred = kmeans.fit_predict(X.drop('Cluster', axis=1))  # drop previous cluster col
    
    inertia.append(kmeans.inertia_)
    sil_scores.append(silhouette_score(X.drop('Cluster', axis=1), y_pred))

# Step 2: Plot Elbow Method (Inertia vs K)
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Inertia (WCSS)')
plt.title('Elbow Method')

# Step 3: Plot Silhouette Score vs K
plt.subplot(1,2,2)
plt.plot(K_range, sil_scores, 'go-')
plt.xlabel('Number of clusters (K)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis')

plt.tight_layout()
plt.show()

# Step 4: Print best K
best_k = K_range[sil_scores.index(max(sil_scores))]
print("Best K (by Silhouette):", best_k)


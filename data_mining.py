import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import streamlit as st


features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    # cluster_std=5,
    random_state=42
)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# kmeans = KMeans(
#     init="random",
#     n_clusters=3,
#     n_init=10,
#     max_iter=300,
#     random_state=42
# )

kmeans_kwargs = {
    "init": "random",
    "n_init": 10,
    "max_iter": 300,
    "random_state": 42,
}

silhouette_coefficients = []
   # Notice you start at 2 clusters for silhouette coefficient
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scaled_features)
    score = silhouette_score(scaled_features, kmeans.labels_)
    silhouette_coefficients.append(score)


plt.style.use("fivethirtyeight")
plt.plot(range(2, 11), silhouette_coefficients)
plt.xticks(range(2, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Coefficient")


st.pyplot(plt)
# a = kmeans.fit(scaled_features)
# print(kmeans.cluster_centers_)
# print(kmeans.n_iter_)
print(kmeans.labels_)
# print(scaled_features[:10])

# print(features)
# print(30 * '--/')
# print(true_labels)



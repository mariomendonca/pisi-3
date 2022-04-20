import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


features, true_labels = make_blobs(
    n_samples=200,
    centers=3,
    cluster_std=2.75,
    # cluster_std=5,
    random_state=42
)

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)


kmeans = KMeans(
    init="random",
    n_clusters=3,
    n_init=10,
    max_iter=300,
    random_state=42
)


a = kmeans.fit(scaled_features)
# print(kmeans.cluster_centers_)
# print(kmeans.n_iter_)
print(kmeans.labels_)
# print(scaled_features[:10])

# print(features)
# print(30 * '--/')
# print(true_labels)

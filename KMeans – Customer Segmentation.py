import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1.Load mall dataset and inspect income and spending score columns.
data = pd.read_csv("Mall_Customers.csv")

print("Dataset Shape:", data.shape)
print(data.head())

# 2.Drop CustomerID column since it does not help clustering.
data_features = data.drop("CustomerID", axis=1)

X = data_features[['Annual Income (k$)', 'Spending Score (1-100)']]

# 3.Apply StandardScaler to features for balanced distance calculation.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4.Run KMeans for multiple values of K and store inertia values.
inertia_values = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia_values.append(kmeans.inertia_)

# 5.Plot elbow curve to decide optimal number of clusters.
plt.figure(figsize=(7,5))
plt.plot(range(1, 11), inertia_values, marker='o')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Optimal K")
plt.show()

#6.Train KMeans with selected K value.

optimal_k = 5   # Change if your elbow shows different K

kmeans_final = KMeans(n_clusters=optimal_k, random_state=42)
clusters = kmeans_final.fit_predict(X_scaled)

# 7.Add cluster labels back into dataset.
data['Cluster'] = clusters

print("\nClustered Data Sample:")
print(data.head())

# 8.Visualize clusters using scatter plot.
plt.figure(figsize=(7,5))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=clusters
)

plt.xlabel("Annual Income (Scaled)")
plt.ylabel("Spending Score (Scaled)")
plt.title("Customer Segmentation Clusters")
plt.show()

# 9.Interpret each cluster and label them as customer types.
data.to_csv("Mall_Customers_Segmented.csv", index=False)

print("\nSegmented dataset saved as Mall_Customers_Segmented.csv")

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = [[1,2],[2,1],[8,8],[9,9]]

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

plt.scatter([i[0] for i in X],[i[1] for i in X],c=kmeans.labels_)
plt.show()
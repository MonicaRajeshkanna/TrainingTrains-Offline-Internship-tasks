from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

X = [[1],[2],[3],[10],[11]]

Z = linkage(X, method='ward')

dendrogram(Z)
plt.show()
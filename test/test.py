import numpy as np
from sklearn.cluster import KMeans


def fun(credit):
    e_p = 1 * np.sin(np.pi * 0.5 * credit) * 0.8
    return e_p


def fun2():
    # 构造数据样本点集X，并计算K-means聚类
    X = np.array([[0, 1], [0, 4], [0, 0], [0, 2], [0, 5], [0, 6]])
    X2 = np.array([(0, 1), (0, 4), (0, 0), (0, 2), (0, 5), (0, 6)])
    X3 = np.array([[0], [1], [2]])
    kmeans = KMeans(n_clusters=1, random_state=0).fit(X3)

    # 输出及聚类后的每个样本点的标签（即类别），预测新的样本点所属类别
    print(kmeans.cluster_centers_[0])


x = (0.334, 0)
cluster_center = (0.88786, 0)
dist = np.sqrt(x[1] ** 2 - cluster_center[1] ** 2)
print(dist)

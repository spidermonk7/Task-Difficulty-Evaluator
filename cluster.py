from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from hodge import *
from evaluation import *

np.random.seed(0)

# --------------------------------
# 画出基于hodgeranking(s)的聚类结果|
# --------------------------------


if __name__ == '__main__':
    for data_file_path in paths:
        print(f"{'='*20} start {'='*20}")
        print(f"now handling data ({data_file_path.split('(')[-1]}")
        # 读取数据
        print(f"reading data from {data_file_path}")
        raw_data_df = pd.read_csv(data_file_path)
        # 计算基本的两两比较数据的统计量（平均值，权重，等）
        Y_raw = get_pair_matrix_Y(raw_data_df)
        Y_3, Y_4 = get_average_Y(Y_raw)
        W = get_weight(Y_raw)
        Y = Y_3  # 选择用Y_3作为Y_raw的平均值

        # 最小二乘求解
        s, residual = get_hodge_solution(Y, W)
        print(f"the s is {s}")
        Cp, Cr = get_inconsistency_index(Y, s, residual, W)
        print(f"inconsistency index, Cp: {Cp}")

        n_clusters=5

        s_sorted = np.sort(s)
        index = np.argsort(s)
 
        X = s.reshape(-1, 1)

        # sort X and get the index
        X_sorted = np.sort(X)
        index = np.argsort(X)
        # print(f"X_sorted: {X_sorted}")
        cluster = KMeans(n_clusters=n_clusters,random_state=0).fit(X)


        for i in range(n_clusters):
            print(np.where([cluster.labels_==i])[1].tolist(), ',')

        y_pred = cluster.labels_#获取训练后对象的每个样本的标签
        centroid = cluster.cluster_centers_
        color=['red','pink','orange','gray','blue']
        fig, axi1=plt.subplots(1)
        for i in range(n_clusters):
            for j in range(X[y_pred==i].shape[0]):
                axi1.scatter(X[y_pred==i][j], 0,
                    marker='o',
                    s=8,
                    c=color[i])

        for i in range(n_clusters):
            axi1.scatter(centroid[i, 0],0,marker='x',s=100,c='black')
            print(centroid[i])

    plt.show()
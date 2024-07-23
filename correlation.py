import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_ana import read_data, load_data
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, Normalize


# 计算
# （1）人类评级和HodgeRank+Cluster的相关性 check_corelation
# （2）人类评级和HodgeRank+Cluster的一致性 check_order（平均评级误差）
# （3）Hodgerank+Cluster和统计数据的一致性 check_data + plot_res_data_consistency


# Data
a = {
'Human Label':
[[0, 3, 4, 6, 8, 10, 12, 13, 16, 36], 
 [1, 15, 17, 20, 22, 23, 26, 27, 28, 33, 47, 51, 52, 53, 56, 59, 66], 
 [2, 5, 9, 11, 14, 18, 19, 25, 30, 34, 40, 41, 42, 44, 45, 46, 54, 60, 63, 65, 67],
[7, 24, 29, 32, 37, 39, 48, 49, 62, 64, 68], 
[21, 31, 35, 38, 43, 50, 55, 57, 58, 61, 69]
],
# 'CSY1':[
#         [4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 30, 34, 36, 42], 
#         [0, 3, 12, 13, 16, 18, 19, 23, 25, 26, 27, 28, 39, 41, 59, 60, 61, 63],
#         [15, 17, 21, 24, 29, 31, 33, 35, 37, 38, 40, 43, 56], 
#         [1, 2, 11, 46, 51, 52, 53, 65, 66, 68], 
#         [32, 44, 45, 47, 48, 49, 50, 54, 55, 57, 58, 62, 64, 67, 69]
#     ],

'HodgeRank+Cluster':[
    [0, 3, 4, 6, 10, 16, 22], 
    [1, 2, 7, 8, 12, 13, 14, 15, 17, 23, 25, 29, 30, 34, 36, 41, 55, 59, 63],
    [5, 11, 19, 21, 24, 26, 33, 35, 37, 40, 45, 56, 60],
    [18, 20, 28, 31, 32, 38, 39, 42, 44, 47, 49, 52, 57, 58, 61, 65, 66, 67, 68],
    [9, 27, 43, 46, 48, 50, 51, 53, 54, 62, 64, 69],
]
}

def check_data(a, type='HodgeRank+Cluster'):
    """
    --------------------------------------------
    Calculate the data consistency between the human label and the HodgeRank+Cluster
    --------------------------------------------
    args:
    (1) a: dict, the data of the human label and the HodgeRank+Cluster
    (2) type: str, the type of the data in [Human Label, HodgeRank+Cluster]
    
    """
    assert type in a
    path = 'data/qs/combined_2.18.csv'
    data = load_data(path)
    dic = read_data(data)
    result = np.zeros((5, 5))
    # result += np.diag(np.ones(5))
    hodge_res = a[type]
    for i in range(4):
        for j in range(i+1, 5):
            inversed = 0
            low_level = hodge_res[i]
            high_level = hodge_res[j]
            for task1 in low_level:
                for task2 in high_level:
                    if task1 < task2:
                        if dic[(task1, task2)][0] > dic[(task1, task2)][1]:
                            inversed += 1
                    elif task1>task2:
                        if dic[(task2, task1)][0] < dic[(task2, task1)][1]:
                            inversed += 1
            inversed/=(len(low_level)*len(high_level))
            result[i, j] = 1 - inversed
    return result

def check_corelation(a):
    """
    --------------------------------------------
    Check the correlation ratio between the human label and the HodgeRank+Cluster
    --------------------------------------------
    args:
    (1) a: dict, the data of the human label and the HodgeRank+Cluster

    return:
    None

    """
    for key in a:
        temp = []
        for i in range(5):
            temp += a[key][i]
        a[key] = temp

    dataframe = pd.DataFrame(a)
    clumn_list = ['Human Label', 'HodgeRank+Cluster']

    # 绘制特征之间的散点图
    sns.pairplot(dataframe[clumn_list], kind="scatter")
    plt.savefig('figs/scatter_plot.png')

    # 计算特征之间的相关性并绘制热力图
    plt.figure(figsize=(25, 7))
    plt.subplot(1, 3, 1)
    correlation_matrix = dataframe[clumn_list].corr(method='pearson')
    # adjust the word size    
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, annot_kws={'size': 20})
    plt.title('Pearson Correlation Heatmap')
    plt.subplot(1, 3, 2)
    correlation_matrix = dataframe[clumn_list].corr(method='kendall')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, annot_kws={'size': 20})
    plt.title('Kendall nCorrelation Heatmap')
    plt.subplot(1, 3, 3)
    correlation_matrix = dataframe[clumn_list].corr(method='spearman')
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, annot_kws={'size': 20})
    plt.title('Spearman Correlation Heatmap')

    # plt.show()
    plt.savefig('figs/correlation_heatmap.png')

def check_order(a):
    """
    --------------------------------------------
    Check the level error
    The level error is calculated by the difference between the human label and the HodgeRank+Cluster
    --------------------------------------------
    For task t:
    human level: Ht
    hodge level: Ht'
    error = |Ht - Ht'|
    Average error = sum(error)/70
    """
    my_list = a['Human Label']
    hodge_list = a['HodgeRank+Cluster']

    my_dic = {}
    hodge_dic = {}
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            my_dic[my_list[i][j]] = i
        for k in range(len(hodge_list[i])):
            hodge_dic[hodge_list[i][k]] = i
    error = 0
    # print(f"my_dic: {my_dic}")
    # print(f"hodge_dic: {hodge_dic}")
    for key in my_dic:
        error += abs(my_dic[key] - hodge_dic[key])
        
    print('error(levels):', error/70)    
    
def plot_res_data_consistency(result, path='figs/level_wise_data_consistency.png'):
    """
    --------------------------------------------
    Check the level-wise consistency of the data, levels are calculated by the hodgerank+cluster
    --------------------------------------------
    W
    args:
    (1) a: dict, the data of the human label and the HodgeRank+Cluster
    (2) path: str, the path to save the plot
    
    """
    matrix = result
    # Define the custom colormap
    colors = [(1, 0.9, 0.9), (0.9, 0, 0)]  # RGB tuples for pink to red
    n_bins = 20  # Discretizes the interpolation into 100 steps
    custom_cmap = LinearSegmentedColormap.from_list(name='custom_red', colors=colors, N=n_bins)

    # Mask zeros to distinguish them clearly (optional)
    masked_matrix = np.ma.masked_where(matrix == 0, matrix)

    # Mask zeros to distinguish them clearly (optional)
    masked_matrix = np.ma.masked_where(matrix == 0, matrix)

    # # Normalize the colormap to the range [0.6, 0.9]
    # norm = Normalize(vmin=0.6, vmax=0.9)

    # Plotting the matrix with the custom colormap and normalization
    plt.imshow(masked_matrix, cmap=custom_cmap, interpolation='nearest')

    # Adding color bar
    plt.colorbar(label='Value')
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i == j:
                plt.gca().add_patch(plt.Rectangle((i - 0.5, i - 0.5), 1, 1, color=(0.93,0.93,0.93), lw=0))
            if i<j:
                plt.gca().add_patch(plt.Rectangle((i - 0.5, j - 0.5), 1, 1, color=(0.93,0.93,0.93), lw=0))

    # Adding text annotations for each cell
    for (i, j), val in np.ndenumerate(matrix):
        if val != 0:  # Skip the zero values for annotations
            plt.text(j, i, f'{val:.2f}', ha='center', va='center', color='black' if val < 0.75 else 'white')
        if i >= j:
            plt.text(j, i, f'----', ha='center', va='center', color='black' if val < 0.75 else 'white')
            # set a light corlor for the diagonal

    # Remove the axis lines (spines) but keep the labels
    ax = plt.gca()
  
    plt.xticks(np.arange(matrix.shape[1]), labels=np.arange(1, matrix.shape[1] + 1))
    plt.yticks(np.arange(matrix.shape[0]), labels=np.arange(1, matrix.shape[0] + 1))


    # Display the plot
    plt.title("Level-wise data consistency comparison")
    plt.show()
    # plt.savefig(path)


if __name__ == '__main__':
    result = check_data(a)
    plot_res_data_consistency(result=result)
    # check_corelation(a)
    # check_order(a)
import pandas as pd
import numpy as np
import numpy as np
from scipy.optimize import minimize
from matplotlib import pyplot as plt
from scipy.interpolate import make_interp_spline

# -----------------------------------------
# 根据计算出的s值求解五个能力集的ability mass|
# -----------------------------------------


def load_xlsx(path):
    data = pd.read_excel(path)
    return data

def extract_task_ability_pair(data, marker='GT'):
    dic = {}
    spliter = ' '
    ability_col = f'Required Ability({marker})'
    assert marker in ['GT', 'GPT4o', 'GPT3.5', 'GPT4']
    if marker == 'GPT4o' or marker=='GPT3.5':
        spliter = ','
        
    for row in data.iterrows():
        if type(row[1][ability_col]) != str:
            dic[row[1]['index']] = [row[1][ability_col]]
        else:
            dic[row[1]['index']] = [int(val) for val in row[1][ability_col].split(spliter)]

    return dic

def fetch_task_ability_pair(data, id):
    for row in data.iterrows():
        if row[1]['index'] == id:
            return (row[1]['index'], row[1]['Task name'], row[1]['Required Ability'])
    
path = 'data/source/AK_marked_v4.xlsx'
data = load_xlsx(path)
marker = 'GT'

dic = extract_task_ability_pair(data, marker=marker)
# 计算出的70个任务的s值(由cluster.py计算得到)
s = [-0.6672563874156494, -0.31292387300189234, -0.3747768685453051, -0.5932192896097728, -0.7818293148136716, -0.02886179159615257, -0.6490937158949027, -0.2045583925727929, -0.2952467800424811, 0.5852645447578632, -0.5890594325064331, -0.1365415165807757, -0.21376197747935938, -0.3629847320754949, -0.2891692879577607, -0.1918461300804619, -0.6780938715140045, -0.21764550409761171, 0.11744072985735314, -0.11416079428341515, 0.11624459108826216, -0.022189341374330738, -0.4811964269630615, -0.24809494591937606, -0.13847951332665123, -0.1927882762658033, -0.10666384978543528, 0.535904880394268, 0.20526455106846372, -0.37799363262764824, -0.19404290460012585, 0.3180860654977551, 0.11459142985578243, -0.0621094924379673, -0.3423531836998627, 0.042642763083779844, -0.24158304367757316, -0.03374048325206536, 0.16104833870902016, 0.32960554044363, -0.014450526909995683, -0.2772822392450799, 0.13485003457149833, 0.5638745042864997, 0.1881744668048225, -0.14674471987254925, 0.39189810181512436, 0.26063457674705154, 0.41810876150084486, 0.14630276611672854, 0.5101560204583445, 0.47747962649834974, 0.3005072446882672, 0.43466522040159433, 0.5078018522668665, -0.2766349434812061, -0.0703220846778818, 0.19174126747124035, 0.23372489245246036, -0.34657016733312007, -0.11252057104303362, 0.30586765668253396, 0.7425201825520881, -0.2751066563452655, 0.4545082403049548, 0.24950860741854375, 0.35125151765789975, 0.32470077862257063, 0.3317263230134376, 0.6158005858180643]
s = np.array(s)
s -= s.min()

# 定义你的损失函数，x 是一个包含五个元素的数组 [x1, x2, x3, x4, x5]
def loss_function(x, s=s, dic=dic):
    # 你可以在这里定义你的损失函数
    # 例如，一个简单的二次损失函数:
    loss = 0
    for i in range(70):
        ability = []
        for j in [1, 2, 3, 4, 5]:
            if j in dic[i]:
                ability.append(x[j-1])
        ability_weight = np.mean(ability)
        loss += np.square(ability_weight - s[i])

    return loss
    

def calculate_s(ability_valueGT, ability_valueGPT3_5, ability_valueGPT4, ability_valueGPT4o):
    if marker == 'GT':
        ability_value = ability_valueGT
    elif marker == 'GPT3.5':
        ability_value = ability_valueGPT3_5
    elif marker == 'GPT4':
        ability_value = ability_valueGPT4
    elif marker == 'GPT4o':
        ability_value = ability_valueGPT4o
        
    res = []
    for i in range(70):
        ability = []
        for j in [1, 2, 3, 4, 5]:
            if j in dic[i]:
                ability.append(ability_value[j-1])
        ability_weight = np.mean(ability)
        res.append(ability_weight)

    return res


def check_ability_distribution(data, plot=False):
    t_a_paire = extract_task_ability_pair(data, marker='GT')
    dic = {}
    for t_a in t_a_paire:
        for a in t_a_paire[t_a]:
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
    print(dic)
    # sort dic based on key
    dic = dict(sorted(dic.items(), key=lambda x: x[0]))
    
    t_a_GPT4 = extract_task_ability_pair(data, marker='GPT4')
    dic_GPT4 = {}
    for t_a in t_a_GPT4:
        for a in t_a_GPT4[t_a]:
            if a not in dic_GPT4:
                dic_GPT4[a] = 1
            else:
                dic_GPT4[a] += 1
    print(dic_GPT4)
    dic_GPT4 = dict(sorted(dic_GPT4.items(), key=lambda x: x[0]))

    t_a_GPT3_5 = extract_task_ability_pair(data, marker='GPT3.5')
    dic_GPT3_5 = {}
    for t_a in t_a_GPT3_5:
        for a in t_a_GPT3_5[t_a]:
            if a not in dic_GPT3_5:
                dic_GPT3_5[a] = 1
            else:
                dic_GPT3_5[a] += 1
    print(dic_GPT3_5)
    dic_GPT3_5 = dict(sorted(dic_GPT3_5.items(), key=lambda x: x[0]))

    t_a_GPT4o = extract_task_ability_pair(data, marker='GPT4o')
    dic_GPT4o = {}
    for t_a in t_a_GPT4o:
        for a in t_a_GPT4o[t_a]:
            if a not in dic_GPT4o:
                dic_GPT4o[a] = 1
            else:
                dic_GPT4o[a] += 1
    print(dic_GPT4o)
    dic_GPT4o = dict(sorted(dic_GPT4o.items(), key=lambda x: x[0]))

    # Colors for the pie chart
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2C2']

    labels =['Feature Detection\n&\nMatching', 'Object Detection\n&\nSegmentation', 'Spatial\nVision', 'Sequential\nVision', 'Reasoning\nVision']
    # a figure with four subplots
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    x = np.arange(5)
    # plot the pie chart
    axs[0, 0].pie(dic.values(), labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
    axs[0, 0].set_title('GT')
    # plot the pie chart
    axs[0, 1].pie(dic_GPT4.values(), labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
    axs[0, 1].set_title('GPT4')
    # plot the pie chart
    axs[1, 0].pie(dic_GPT3_5.values(), labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
    axs[1, 0].set_title('GPT3.5')
    # plot the pie chart
    axs[1, 1].pie(dic_GPT4o.values(), labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, wedgeprops={'edgecolor': 'black'})
    axs[1, 1].set_title('GPT4o')
    plt.savefig('ability_distribution.png')
    plt.show()



    return dic


def level_wise_ability(data, marker='GT'):
    levels_hodge = [
    [0, 3, 4, 6, 10, 16, 22], 
    [1, 2, 7, 8, 12, 13, 14, 15, 17, 23, 25, 29, 30, 34, 36, 41, 55, 59, 63],
    [5, 11, 19, 21, 24, 26, 33, 35, 37, 40, 45, 56, 60],
    [18, 20, 28, 31, 32, 38, 39, 42, 44, 47, 49, 52, 57, 58, 61, 65, 66, 67, 68],
    [9, 27, 43, 46, 48, 50, 51, 53, 54, 62, 64, 69],
    ]
    levels_csy = [
    [0, 3, 4, 6, 8, 10, 12, 13, 16, 36], 
    [1, 15, 17, 20, 22, 23, 26, 27, 28, 33, 47, 51, 52, 53, 56, 59, 66], 
    [2, 5, 9, 11, 14, 18, 19, 25, 30, 34, 40, 41, 42, 44, 45, 46, 54, 60, 63, 65, 67],
    [7, 24, 29, 32, 37, 39, 48, 49, 62, 64, 68], 
    [21, 31, 35, 38, 43, 50, 55, 57, 58, 61, 69]
    ]


    t_a_pair = extract_task_ability_pair(data, marker=marker)
    print(t_a_pair)    
    dic_level_ability = {}
    for lid, level in enumerate(levels_hodge):
        for t in level:
            for a in t_a_pair[t]:
                if lid not in dic_level_ability:
                    dic_level_ability[lid] = [0, 0, 0, 0, 0]
                dic_level_ability[lid][a-1] += 1
    # normalize the distribution
    for a in dic_level_ability:
        total = sum(dic_level_ability[a])
        dic_level_ability[a] = [val/total for val in dic_level_ability[a]]

    
    dic_level_ability_csy = {}
    for lid, level in enumerate(levels_csy):
        for t in level:
            for a in t_a_pair[t]:
                if lid not in dic_level_ability_csy:
                    dic_level_ability_csy[lid] = [0, 0, 0, 0, 0]
                dic_level_ability_csy[lid][a-1] += 1
    # normalize the distribution
    for a in dic_level_ability_csy:
        total = sum(dic_level_ability_csy[a])
        dic_level_ability_csy[a] = [val/total for val in dic_level_ability_csy[a]]
    print(dic_level_ability_csy)


    # plot the distribution
    abilities = ['Feature Detection\n&\nMatching', 'Object Detection&Segmentation', 'Spatial Vision', 'Sequential Vision', 'Reasoning Vision']
    
    data_hodge = dic_level_ability
    data_csy = dic_level_ability_csy
    
    # 可能的取值为 ability1-5
    abilities = ['ab1', 'ab2', 'ab3', 'ab4', 'ab5']

    # 创建图表
    x = np.arange(len(abilities))  # 能力的索引

    # 为每个分布绘制平滑曲线并填充曲线下方区域
    plt.figure(figsize=(15, 10))
    for key in data_hodge:
        values_hodge = data_hodge[key]
        values_csy = data_csy[key]
        plt.subplot(2, 3, key+1)
        # 生成平滑曲线
        x_smooth = np.linspace(x.min(), x.max(), 300)
        spl = make_interp_spline(x, values_hodge, k=1)  # 使用二次样条插值
        spl_csy = make_interp_spline(x, values_csy, k=1)
        y_smooth = spl(x_smooth)
        y_smooth_csy = spl_csy(x_smooth)
        plt.ylim(0, 0.6)
        # 绘制平滑曲线
        plt.plot(x_smooth, y_smooth, label=f'Ability distirbution(Hodge+Cluster)')
        plt.plot(x_smooth, y_smooth_csy, label=f'Ability distribution(Human)')
        plt.legend()
        plt.fill_between(x_smooth, y_smooth, alpha=0.3)
        plt.fill_between(x_smooth, y_smooth_csy, alpha=0.3)
        plt.xticks(ticks=x, labels=abilities)  # 设置x轴的标签
        plt.title(f'Level {key}')


    # 添加图例
    plt.legend()
    # 标题和坐标轴标签
    # plt.suptitle('Distributions of Different Abilities')
    plt.xlabel('Ability')
    plt.ylabel('Distribution')
    
    plt.savefig(f'smoothed_levelwise_ab_distributions_Both{marker}.png')
    # 显示图表
    plt.show()



    return dic_level_ability


def plot_smoothed_distributions():
    # 提供的数据
    data_hodge = {
        0: [0.5555555555555556, 0.4444444444444444, 0.0, 0.0, 0.0],
        1: [0.16216216216216217, 0.21621621621621623, 0.21621621621621623, 0.1891891891891892, 0.21621621621621623],
        2: [0.08, 0.04, 0.28, 0.24, 0.36],
        3: [0.17647058823529413, 0.029411764705882353, 0.17647058823529413, 0.14705882352941177, 0.47058823529411764],
        4: [0.14285714285714285, 0.14285714285714285, 0.047619047619047616, 0.19047619047619047, 0.47619047619047616]
    }

    data_csy = {0: [0.6, 0.3333333333333333, 0.06666666666666667, 0.0, 0.0], 1: [0.23333333333333334, 0.1, 0.3, 0.1, 0.26666666666666666], 2: [0.07317073170731707, 0.12195121951219512, 0.1951219512195122, 0.2926829268292683, 0.3170731707317073], 3: [0.1, 0.1, 0.1, 0.15, 0.55], 4: [0.05, 0.1, 0.1, 0.2, 0.55]}




    # 可能的取值为 ability1-5
    abilities = ['ab1', 'ab2', 'ab3', 'ab4', 'ab5']

    # 创建图表
    x = np.arange(len(abilities))  # 能力的索引

    # 为每个分布绘制平滑曲线并填充曲线下方区域
    plt.figure(figsize=(15, 10))
    for key in data_hodge:
        values_hodge = data_hodge[key]
        values_csy = data_csy[key]
        plt.subplot(2, 3, key+1)
        # 生成平滑曲线
        x_smooth = np.linspace(x.min(), x.max(), 300)
        spl = make_interp_spline(x, values_hodge, k=1)  # 使用二次样条插值
        spl_csy = make_interp_spline(x, values_csy, k=1)
        y_smooth = spl(x_smooth)
        # y_smooth_csy = spl_csy(x_smooth)
        plt.ylim(0, 0.6)
        # 绘制平滑曲线
        plt.plot(x_smooth, y_smooth, label=f'Abilities Distribution of level {key+1}')
        # plt.plot(x_smooth, y_smooth_csy, label=f'Abilities Distribution of level {key+1}(CSY)')
        plt.legend()
        plt.fill_between(x_smooth, y_smooth, alpha=0.3)
        # plt.fill_between(x_smooth, y_smooth_csy, alpha=0.3)
        plt.xticks(ticks=x, labels=abilities)  # 设置x轴的标签
        plt.title(f'Level {key}')


    # 添加图例
    plt.legend()
    # 标题和坐标轴标签
    plt.suptitle('Smoothed Probability Distributions of Different Abilities')
    plt.xlabel('Ability')
    plt.ylabel('Probability')
    
    plt.savefig('smoothed_levelwise_ab_distributions_Both.png')
    # 显示图表
    plt.show()


history = []
def callback(x):
    f_val = loss_function(x)
    history.append(f_val)
    print(f_val, ',')


if __name__ == '__main__':
    abilities = ['Feature Detection&Matching', 'Object Detection&Segmentation', 'Spatial Vision', 'Sequential Vision', 'Reasoning Vision']
    # 初始猜测
    initial_guess = [0, 0, 0, 0, 0]

    # 使用scipy的minimize函数进行优化, 求解最小化损失函数的ability mass
    result = minimize(loss_function, initial_guess, method='BFGS', callback=callback)
    mass = result.x
    print(f"Optimized mass: {mass}")

    # 计算通过我们方法计算的s值
    s_cal = np.zeros(70)
    for task in dic:
        for ability in dic[task]:
            s_cal[task] += mass[ability-1]      
        s_cal[task] = s_cal[task]/len(dic[task])
        

    # Plot the difference
    plt.figure(figsize=(12, 6))
    plt.plot(s, label='Sampled s', marker='o', linestyle='--', color='green')
    plt.plot(s_cal, label='Calculated s', marker='o', linestyle='-', color='red')
    plt.xlabel('Task Index')
    plt.ylabel('Value')
    plt.title('Sampled D(s) vs. Calculated DA(s)')
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    # plt.savefig(f'figs/sampled_vs_calculated_s_{marker}.png')


    # Calculate delta and handle inf values
    delta_s = np.abs(s - s_cal) / s
    delta_s = np.where(np.isfinite(delta_s), delta_s, np.nan)  # Replace inf with NaN for mean calculation
    # Plot the delta values
    plt.figure(figsize=(12, 6))
    plt.plot(delta_s, label='Delta s', marker='o', linestyle='-', color='green')
    plt.axhline(y=np.nanmean(delta_s), color='red', linestyle='--', label=f'Mean ({np.nanmean(delta_s):.4f})')
    plt.xlabel('Task Index')
    plt.ylabel('Delta Value')
    plt.title('Delta D(s) (Normalized Difference)')
    plt.legend()
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.show()
    plt.savefig(f'figs/delta_s_{marker}.png')

    print(f"Mean delta s: {np.nanmean(delta_s):.4f}")
    
    # plot the bars with different colors
    # x = np.arange(5)
    # plt.bar(x, result.x, color=['red', 'green', 'blue', 'purple', 'orange'])
    # plt.xticks(x, abilities)
    # plt.show()
    # print(marker, result.x)

    # check the ability distribution
    # check_ability_distribution(data, plot=True)

    # level_wise_ability(data)
    # plot_smoothed_distributions()
    
    # print(fetch_task_ability_pair(data, 23))
    # print(fetch_task_ability_pair(data, 41))
    # level_wise_ability(data, marker='GPT4o')
    # level_wise_ability(data, marker='GPT3.5')
    # level_wise_ability(data, marker='GPT4')
    # level_wise_ability(data, marker='GT')
    # plot_smoothed_distributions()
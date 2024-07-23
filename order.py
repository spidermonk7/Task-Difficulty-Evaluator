# check the order
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
def pre_stored_res(cluster_name='hodge'):
    cluster_kmeans = [
        [ 0 , 1,  4 , 5 , 9 ,10, 14 ,16 ,22, 23, 34 ,35 ,40 ,41, 56 ,61],
        [ 6,11 ,26 ,36 ,43 ,57],
        [ 3 ,12, 13 ,19 ,20 ,21 ,37 ,39, 49, 50 ,51 ,52, 54 ,58 ,59 ,63, 67, 68],
        [ 2 , 7, 15, 18 ,24 ,25, 29 ,30, 33, 38, 42, 45, 47 ,48, 53, 55, 60, 66],
        [ 8, 17, 27, 28, 31, 32, 44 ,46 ,62 ,64 ,65, 69]
    ]

    cluster_csy = [
        [4, 5, 6, 7, 8, 9, 10, 14, 20, 22, 30, 34, 36, 42], 
        [0, 3, 12, 13, 16, 18, 19, 23, 25, 26, 27, 28, 39, 41, 59, 60, 61, 63],
        [15, 17, 21, 24, 29, 31, 33, 35, 37, 38, 40, 43, 56], 
        [1, 2, 11, 46, 51, 52, 53, 65, 66, 68], 
        [32, 44, 45, 47, 48, 49, 50, 54, 55, 57, 58, 62, 64, 67, 69]
    ]

    cluster_yp = [
        [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 47], 
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 63], 
        [7, 21, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 61, 64, 65],
        [45, 48, 49, 51, 52, 54, 55, 56, 62, 66, 67, 68, 69], 
        [46, 50, 53, 57, 58, 59, 60]
    ]


    cluster_jh = [
        [0, 3, 4, 5, 6, 8, 9, 12, 20, 23], 
        [13, 14, 15, 16, 17, 18, 19, 25, 29, 34, 35, 39, 42, 44, 59, 61, 63], 
        [1, 2, 7, 11, 21, 22, 24, 27, 28, 30,31, 38, 40, 43, 48, 51, 53, 57, 58, 60, 67],
        [10, 33, 36, 37, 41, 45, 46, 47, 49, 50, 52, 54, 55, 56,  64, 65 ,66, 68, 69],
        [26, 32, 62]
    ]
    

    cluster_bert = [ 
        [1, 12, 13, 14, 18, 19, 30, 33, 35, 53, 57, 65],
        [3, 6, 8, 10, 11, 15, 16, 22, 25, 29, 36, 37, 41, 42, 50, 55, 56, 59, 62],                       
        [0, 2, 4, 5, 17, 21, 23, 26, 28, 40, 43, 44, 45, 47, 48, 52, 58, 60, 61, 63, 64, 66, 68],               
        [9, 20, 31, 32, 34, 38, 39, 49, 54, 67, 69], 
        [7, 24, 27, 46, 51], 
    ]
    
    cluster_hodge = [
        [0, 1, 4, 5, 6, 9, 10, 11, 14, 16, 22, 23, 34, 35, 40, 41, 56, 57, 61] ,
        [3, 12, 13, 19, 20, 21, 26, 36, 39, 43, 50, 51, 54, 58, 59, 67] ,
        [2, 7, 29, 30, 37, 38, 45, 49, 52, 55, 60, 63, 66, 68] ,
        [8, 15, 17, 18, 24, 25, 31, 33, 42, 46, 47, 48, 53, 65] ,
        [27, 28, 32, 44, 62, 64, 69]
    ]

    if cluster_name == 'kmeans':
        return cluster_kmeans
    elif cluster_name == 'csy':
        return cluster_csy
    elif cluster_name == 'yp':
        return cluster_yp
    elif cluster_name == 'jh':
        return cluster_jh
    elif cluster_name == 'bert':
        return cluster_bert
    elif cluster_name == 'hodge':
        return cluster_hodge
    else:
        print('cluster_name is not valid')
        return None


# Function to process the data and create the taskpair - choices collection
def process_data(file_path):
    # Load the data
    if 'filted' in file_path:
        data = pd.read_excel(file_path)
    else:
        data = pd.read_csv(file_path)
    item_num = len(data['taskA_ids'])
    dic = {}
    for interviewee in range(len(data['taskA_ids'])):
        if interviewee >=110:
            taskAs = data['taskA_ids'][interviewee].split(', ')
            taskBs = data['taskB_ids'][interviewee].split(', ')
            choices = data['choices'][interviewee].split(',')
            # print(taskAs)
            # print(taskBs)
            # print(choices)
        elif interviewee <110:
            taskAs = data['taskA_ids'][interviewee].split(',')
            taskBs = data['taskB_ids'][interviewee].split(',')
            choices = data['choices'][interviewee].split(',')
            # print(taskAs)
            # print(taskBs)
            # print(choices)
        for taskA, taskB, choice in zip(taskAs, taskBs, choices):
            taskA, taskB = int(taskA), int(taskB)
            choice = int(choice)
            # print(taskA, taskB, choice)
            if taskB < taskA:
                taskA, taskB = taskB, taskA 
                if choice == 1:
                    choice = 2
                elif choice == 2:
                    choice = 1
            
            if str((taskA, taskB)) not in dic:
                dic[str((taskA, taskB))] = [0, 0, 0]
                if choice == 1:
                    dic[str((taskA, taskB))][0] += 1
                elif choice == 2:
                    dic[str((taskA, taskB))][1] += 1
                else:
                    dic[str((taskA, taskB))][2] += 1

            else:
                if choice == 1:
                    dic[str((taskA, taskB))][0] += 1
                elif choice == 2:
                    dic[str((taskA, taskB))][1] += 1
                else:
                    dic[str((taskA, taskB))][2] += 1

    return dic, item_num

def res_check(cluster_name='hodge'):
    cluster = pre_stored_res(cluster_name)
    if cluster is None:
        return False
    cnt = 0
    check_list = np.ones(70)

    for i in range(len(cluster)):
        for j in range(len(cluster[i])):
            cnt += 1
            check_list[cluster[i][j]] = 0

    if cnt ==70:
        print('res is valid: ', cluster_name)
        return True
    print('res is invalid: ', cluster_name, np.where(check_list == 1))
    return False


def calculate_level_error(clusters1, clusters2):
    error = 0
    max_error = 0
    for task in range(70):
        for id in range(5):
            if task in clusters1[id]:
                id1 = id
            if task in clusters2[id]:
                id2 = id

        error = error + abs(id1 - id2)
        max_error = max(max_error, abs(id1 - id2))
    mean_error = error / 70
    return {'mean_error': mean_error, 'max_error': max_error}


def calculate_order_error(cluster, dic):
    error_set = {}
    level_set = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    level_set = {1:[], 2:[], 3:[], 4:[], 5:[]}
    res = np.zeros((5, 5))
    for i in [0, 1, 2, 3]:
        for j in range(i+1, 5):
            clu1 = cluster[i]
            clu5 = cluster[j]
            wrong = 0
            for taskA in clu1:
                for taskB in clu5:
                    if taskA < taskB:
                        key = str((taskA, taskB))
                        if key not in dic:
                            continue
                        try:
                            rateAharder = dic[key][0] / (dic[key][0] + dic[key][1]+dic[key][2])
                            rateBharder = dic[key][1] / (dic[key][1] + dic[key][0]+dic[key][2])
                        except:
                            print(key, dic[key])
                        
                        if rateAharder > rateBharder:
                            if taskA not in level_set[i+1]:
                                level_set[i+1].append(taskA)
                            if taskB not in level_set[j+1]:
                                level_set[j+1].append(taskB)

                            wrong += 1
                            if taskA in error_set:
                                error_set[taskA] += 1
                            else:
                                error_set[taskA] = 1
                            if taskB in error_set:
                                error_set[taskB] += 1
                            else:
                                error_set[taskB] = 1
                                # print(f"found a highly wrong pair: ({taskA}, {taskB}) at level ({i+1}, {j+1}) respectively with rateAharder: {rateAharder}, rateBharder: {rateBharder}")
                    elif taskA > taskB:
                        key = str((taskB, taskA))
                        if key not in dic:
                            continue
                        try:
                            rateBharder = dic[key][0] / (dic[key][0] + dic[key][1]+dic[key][2])
                            rateAharder = dic[key][1] / (dic[key][1] + dic[key][0]+dic[key][2])
                        except:
                            print(key, dic[key])
                        if rateAharder > rateBharder:
                            wrong += 1
                            if taskA not in level_set[i+1]:
                                level_set[i+1].append(taskA)
                            if taskB not in level_set[j+1]:
                                level_set[j+1].append(taskB)
                                
                            if taskA in error_set:
                                    error_set[taskA] += 1
                            else:
                                error_set[taskA] = 1
                            if taskB in error_set:
                                error_set[taskB] += 1
                            else:
                                error_set[taskB] = 1
                                # print(f"found a highly wrong pair: ({taskA}, {taskB}) at level ({i+1}, {j+1}) respectively with rateAharder: {rateAharder}, rateBharder: {rateBharder}")
            res[i][j] = 1 - wrong/(len(clu1) * len(clu5))

    # for i in range(5):
    #     normalizer = 0
    #     for j in range(5):
    #         if j != i:
    #             normalizer += len(cluster[j])
    #     level_set[i+1] = level_set[i+1] / (len(cluster[i])*normalizer)

    return res, error_set, level_set



def get_clusters_majorwise(major = 'all'):
    if major == 'E':
        return [
                [4, 5, 6, 12, 16, 22, 23, 26, 34, 56, 59] ,
                [2, 8, 13, 15, 17, 18, 19, 24, 29, 30, 33, 37, 38, 45, 46, 50, 51, 53, 54, 60, 67, 68] ,
                [3, 7, 11, 20, 21, 25, 36, 39, 42, 43, 49, 52, 55, 57, 58, 63, 66] ,
                [0, 1, 9, 10, 14, 35, 40, 41, 61] ,
                [27, 28, 31, 32, 44, 47, 48, 62, 64, 65, 69] ,
        ]
    
    if major == 'not-E':
        return [
                [27, 28, 32, 44, 62, 64, 69] ,
                [0, 1, 4, 5, 6, 9, 10, 11, 14, 16, 22, 23, 34, 35, 40, 41, 56, 57, 61] ,
                [2, 29, 30, 37, 38, 45, 47, 49, 52, 55, 60, 63, 66] ,
                [3, 12, 13, 19, 20, 21, 26, 36, 39, 43, 50, 51, 54, 58, 59, 67, 68] ,
                [7, 8, 15, 17, 18, 24, 25, 31, 33, 42, 46, 48, 53, 65]
        ]



    if major == 'all':
        return [[3, 12, 13, 19, 20, 21, 26, 36, 39, 43, 50, 51, 54, 58, 59, 67] ,
                [8, 15, 17, 18, 24, 25, 31, 33, 42, 46, 47, 48, 53, 65] ,
                [0, 1, 4, 5, 6, 9, 10, 11, 14, 16, 22, 23, 34, 35, 40, 41, 56, 57, 61] , 
                [2, 7, 29, 30, 37, 38, 45, 49, 52, 55, 60, 63, 66, 68] ,
                [27, 28, 32, 44, 62, 64, 69]]
    
    if major == 'CA':
        return [
            [17, 24, 25, 28, 31, 32, 38, 44, 46, 48, 50, 53, 64, 65, 66] ,
            [3, 6, 11, 12, 13, 14, 16, 19, 20, 21, 23, 36, 41, 45, 57, 59, 61, 63] ,
            [0, 1, 4, 5, 9, 10, 22, 34, 35, 39, 40] ,
            [2, 7, 8, 15, 18, 26, 29, 30, 33, 37, 42, 43, 47, 49, 51, 52, 54, 55, 56, 58, 60, 67, 68] ,
            [27, 62, 69] ,
        ]
    
    if major == 'not-CA':
        return [
            [1, 4, 5, 6, 11, 12, 16, 23, 26, 34, 36, 40, 43, 57, 58, 59] ,
            [2, 7, 8, 15, 17, 18, 24, 25, 31, 33, 42, 46, 47, 48, 53] ,
            [27, 28, 32, 44, 62, 64, 65, 69] ,
            [3, 13, 19, 20, 21, 29, 30, 37, 38, 39, 45, 49, 50, 51, 52, 54, 55, 60, 63, 66, 67, 68] ,
            [0, 9, 10, 14, 22, 35, 41, 56, 61]
        ]


    if major == 'CAN':
        return [[7, 13, 15, 26, 29, 30, 42, 43, 45, 49, 51, 54, 55, 58, 59, 60, 63, 67, 68] ,
                [0, 1, 5, 9, 10, 34, 35] ,
                [17, 27, 28, 32, 44, 46, 48, 53, 62, 64, 65, 69] ,
                [3, 4, 6, 11, 12, 14, 16, 19, 20, 21, 22, 23, 36, 39, 40, 41, 56, 57, 61] ,
                [2, 8, 18, 24, 25, 31, 33, 37, 38, 47, 50, 52, 66]
                ]
    
    if major == 'not-CAN':
        return [
                [2, 3, 13, 19, 20, 21, 30, 37, 38, 39, 45, 49, 52, 55, 60, 63, 66, 68] ,
                [7, 8, 15, 17, 18, 24, 25, 29, 31, 33, 42, 46, 47, 48, 53, 65] ,
                [0, 1, 4, 5, 6, 9, 10, 11, 14, 22, 23, 26, 34, 35, 40, 41, 56, 57, 61] ,
                [27, 28, 32, 44, 62, 64, 69] ,
                [12, 16, 36, 43, 50, 51, 54, 58, 59, 67]
                ]
    
    if major == 'not-CANE':
        return [
                [6, 16, 36, 40, 43, 50, 51, 54, 58, 59, 67] ,
                [8, 18, 27, 28, 32, 44, 62, 64, 69] ,
                [2, 3, 12, 13, 19, 20, 21, 30, 37, 38, 39, 45, 47, 49, 52, 55, 60, 63, 66, 68] ,
                [0, 1, 4, 5, 9, 10, 11, 14, 22, 23, 26, 34, 35, 41, 56, 57, 61] ,
                [7, 15, 17, 24, 25, 29, 31, 33, 42, 46, 48, 53, 65]
                ]

    if major == 'not-CAE':
        return [
                [0, 1, 4, 5, 6, 9, 10, 11, 14, 16, 22, 23, 26, 34, 35, 40, 41, 56, 57, 61] ,
                [7, 8, 15, 17, 18, 24, 25, 31, 33, 42, 46, 48, 53] ,
                [12, 36, 43, 50, 51, 54, 58, 59, 67, 68] ,
                [27, 28, 32, 44, 62, 64, 65, 69] ,
                [2, 3, 13, 19, 20, 21, 29, 30, 37, 38, 39, 45, 47, 49, 52, 55, 60, 63, 66] 
                ]
    if major == 'not-CHANE':
        return [
                [8, 18, 27, 28, 32, 44, 62, 64, 65, 69] ,
                [3, 12, 13, 19, 20, 21, 30, 37, 38, 39, 45, 47, 49, 52, 55, 60, 66, 68] ,
                [0, 9, 11, 14, 22, 23, 34, 35, 56, 57, 61] ,
                [2, 7, 15, 17, 24, 25, 29, 31, 33, 42, 46, 48, 53, 63] ,
                [1, 4, 5, 6, 10, 16, 26, 36, 40, 41, 43, 50, 51, 54, 58, 59, 67] 
                ]

    if major == 'CANE':
        return [[7, 8, 13, 15, 18, 25, 29, 30, 33, 37, 42, 43, 45, 49, 50, 51, 52, 54, 55, 60, 66, 67, 68] ,
                [3, 4, 11, 12, 14, 16, 19, 20, 21, 23, 26, 36, 39, 56, 57, 58, 59, 63] ,
                [27, 28, 32, 44, 62, 64, 69] ,
                [0, 1, 5, 6, 9, 10, 22, 34, 35, 40, 41, 61] ,
                [2, 17, 24, 31, 38, 46, 47, 48, 53, 65]] 
    
    if major == 'CAE':
        return [[0, 1, 4, 5, 6, 9, 10, 12, 14, 22, 34, 35, 40, 41, 61] ,
                [2, 8, 15, 18, 24, 25, 29, 30, 33, 37, 42, 45, 49, 50, 51, 52, 54, 55, 58, 60, 66, 67, 68] ,
                [3, 7, 11, 13, 16, 19, 20, 21, 23, 26, 36, 39, 43, 56, 57, 59, 63] ,     
                [62] ,
                [17, 27, 28, 31, 32, 38, 44, 46, 47, 48, 53, 64, 65, 69] ]
    if major == 'CHANE':
        return [[2, 7, 15, 29, 30, 37, 42, 45, 49, 50, 51, 52, 54, 55, 60, 66, 67, 68] ,
                [3, 11, 12, 13, 19, 20, 21, 23, 26, 36, 39, 43, 56, 57, 58, 59, 63] ,
                [27, 28, 32, 44, 62, 64, 69] ,
                [8, 17, 18, 24, 25, 31, 33, 38, 46, 47, 48, 53, 65] ,
                [0, 1, 4, 5, 6, 9, 10, 14, 16, 22, 34, 35, 40, 41, 61]
                ]



def consistency_check(major='CA'):
    print(f"Now we are checking major combination: {major}")
    unchecked_pair = []
    compared_times = []
    path = f'./data/acceptable-data({major}).csv'
    # path = f'./data/filted_data.xls'
    dic, item_num = process_data(path)
    totally_consist = 0
    weak_consist = 0
    for i in range(70):
        for j in range(i+1, 70):
            key = str((i, j))
            if key not in dic:
                unchecked_pair.append((i, j))
                continue
            compared_times.append(dic[key][0] + dic[key][1] + dic[key][2])
            if (dic[key][0]==0 and dic[key][1]!=0) or (dic[key][0]!=0 and dic[key][1]==0):
                # print(f"dic[{key}]: {dic[key]}")
                totally_consist += 1
                
    print(f"unchecked pair: {len(unchecked_pair)}") 
    print(f"compared times: {np.mean(np.array(compared_times))}")
    
    return unchecked_pair, np.array(compared_times).mean(), totally_consist/len(compared_times)
if __name__ == '__main__':
    # Use the function with your file path
    cluster_csy = pre_stored_res('csy')

    cluster_hodge = pre_stored_res('hodge')
    cluster_jp = pre_stored_res('yp')
    cluster_jh = pre_stored_res('jh')


    cluster_hodge_ca = [
        [17, 24, 25, 28, 31, 32, 38, 44, 46, 48, 50, 53, 64, 65, 66] ,
        [3, 6, 11, 12, 13, 14, 16, 19, 20, 21, 23, 36, 41, 45, 57, 59, 61, 63] ,
        [0, 1, 4, 5, 9, 10, 22, 34, 35, 39, 40] ,
        [2, 7, 8, 15, 18, 26, 29, 30, 33, 37, 42, 43, 47, 49, 51, 52, 54, 55, 56, 58, 60, 67, 68] ,
        [27, 62, 69]
    ]


    res_dic = {}
    for group in [('C', 'not-C')]:
        tmp = []
        for idx, major in enumerate(group):
            print('-------------------')
            # print(f"handling {major}")
            # cluster_major = get_clusters_majorwise(major)
            # res2 = calculate_level_error(cluster_csy, cluster_major)
            # print(f'error for {major} is: ', res2)
            file_path = f'./data/acceptable-data({major}).csv'
            if major == 'all':
                file_path = './data/filted_data.xls'
            dic, item_num = process_data(file_path)
            res, error_set, level_set = calculate_order_error(cluster_csy, dic)
            tmp.append(np.sum(res)/10) 
            break
        # res_dic[group] = (tmp[0], tmp[1])
    
    # print(res_dic)
    # calculate the mean of  error_set, get all key that higher than mean
    print(f"the mean is {np.mean(list(error_set.values()))}")
    error_set = {k: v for k, v in error_set.items() if v > np.mean(list(error_set.values()))}   
    print(error_set) 
    # sort key based on values
    error_set = dict(sorted(error_set.items(), key=lambda item: item[1], reverse=True))
    print(error_set)
    path = f'./data/discrimination.csv'
    try:
        df = pd.read_csv(path, encoding='gbk')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(path, encoding='ISO-8859-1')
        except UnicodeDecodeError:
            df = pd.read_csv(path, encoding='gbk')
    print(df)
    p_s = {'Instructed':0, 'Autonomic':0}
    p_s_all = {'Instructed':0, 'Autonomic':0}
    for row in df.iterrows():
        if row[1]['指令/自主'] == '指令':
            p_s_all['Instructed'] += 1
            if row[0] in error_set:
                p_s['Instructed'] += 1
        else:
            p_s_all['Autonomic'] += 1
            if row[0] in error_set:
                p_s['Autonomic'] += 1


    print(p_s_all)
    print(p_s)
    p_s = {k: v/p_s_all[k] for k, v in p_s.items()}
    print(p_s)
    # res_dic = {}    
    # for combination in ['C','CN', 'CE', 'CNE', 'CNEH']:
    #     print('-------------------')
    #     key = (combination, f'not-{combination}')
    #     unchecked_pair, compared_times, consistency_rate = consistency_check(combination)
    #     not_unchecked_pair, not_compared_times, not_consistency_rate = consistency_check(f'not-{combination}')
    #     res_dic[key] = ((unchecked_pair, not_unchecked_pair), (compared_times, not_compared_times), (consistency_rate, not_consistency_rate))

    # # plot res_dic[key][0], each key and value is a tuple, make sure their bar are closely next to each other
    
    
    # print('{')
    # for key in res_dic:
    #     print(key,":", res_dic[key][2], end=',')

    # print('}')
    # plt.bar(res_dic.keys(), [res_dic[key][2] for key in res_dic.keys()])
    # plt.ylim(0.5, 0.8)
    # plt.title('strong consistency rate')

    # plt.show()
 
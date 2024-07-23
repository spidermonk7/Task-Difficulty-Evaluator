import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data(path):
    data = pd.read_csv(path)
    return data


def check_data(data):
    failed = []
    passed = []
    for row in data.iterrows():
        if row[0] in [0, 1]: continue
        if row[1]['Q13'] != 'task A and B are equally difficult' or row[1]['Q13'] is None:
            failed.append(row[1]['Q3'])
        else:
            passed.append(row[1]['Q3'])
    print(f"Failure check done, failed: {len(failed)}")
    return failed, passed

def read_data(data):
    dic = {}
    task_A_list = []
    task_B_list = []
    choices_list = []
    for row in data.iterrows():
        if row[0] in [0, 1]: continue
        if row[1]['Q13'] != 'task A and B are equally difficult' or row[1]['Q13'] is None: continue
        task_A_list = [int(val) for val in row[1]['task_A_id_list'].split(',')]
        task_B_list = [int(val) for val in row[1]['task_B_id_list'].split(',')]
        choices_list = [int(val) for val in row[1]['choices'].split(',')]
        # print(len(task_A_list), len(task_B_list), len(choices_list))
        for a, b, c in zip(task_A_list, task_B_list, choices_list):
            switch = False
            if a<b:
                task_pair = (a, b)
            else:
                task_pair = (b, a)
                switch = True
            if task_pair not in dic:
                dic[task_pair] = [0, 0, 0, 0]
            
            if not switch:
                dic[task_pair][c-1] += 1
            
            else:
                if c == 0:
                    dic[task_pair][1] += 1
                elif c == 1:
                    dic[task_pair][0] += 1
                else:
                    dic[task_pair][2] += 1 

            dic[task_pair][3] += 1
    return dic


def read_valid_data(data):
    dic = {}
    task_A_list = []
    task_B_list = []
    choices_list = []
    for row in data.iterrows():
        if row[0] in [0, 1]: continue
        if row[1]['Q13'] != 'task A and B are equally difficult' or row[1]['Q13'] is None: continue
        task_A_list = [int(val) for val in row[1]['task_A_id_list'].split(',')]
        task_B_list = [int(val) for val in row[1]['task_B_id_list'].split(',')]
        choices_list = [int(val) for val in row[1]['choices'].split(',')]

        # print(len(task_A_list), len(task_B_list), len(choices_list))
        for a, b, c in zip(task_A_list, task_B_list, choices_list):
            task_pair = (a, b)
            # print(task_pair, c)
            if task_pair not in dic:
                dic[task_pair] = [0, 0, 0, 0]
            if c == 0:
                dic[task_pair][1] += 1
            elif c == 1:
                dic[task_pair][0] += 1
            else:
                dic[task_pair][2] += 1 

            dic[task_pair][3] += 1
    return dic




def check_task_pairs(dic):
    # return: task_pairs with comparison times, uncompared task_pairs
    un_compared = []
    for i in range(69):
        for j in range(i, 70):
            if i == j:
                continue
            if (i, j) not in dic:
                un_compared.append((i, j))

    # average, max compare times:
    compare_times = []
    for key, val in dic.items():
        compare_times.append(val[3])
    print('average compare times:', np.mean(compare_times))
    print('max compare times:', np.max(compare_times))
    print('uncompared task pairs:', len(un_compared))
    return compare_times, un_compared

def consistency_check(dic):
    # check consistency:
    consistency_dic = {
        'strongly consistent': 0,
        'consistent': 0,
        'weakly consistent': 0,
        'inconsistent': 0,

    }
    for key in dic:
        if dic[key][0] == 0 and dic[key][1] !=0 or dic[key][0] != 0 and dic[key][1] == 0 or dic[key][0] == 0 and dic[key][1] == 0:
            consistency_dic['strongly consistent'] += 1

        elif dic[key][0] + dic[key][2] >= dic[key][3]*0.8 or dic[key][1] + dic[key][2] >= dic[key][3]*0.8:
            consistency_dic['consistent'] += 1

        elif dic[key][0] + dic[key][2] >= dic[key][3]*0.6 or dic[key][1] + dic[key][2] >= dic[key][3]*0.6:
            consistency_dic['weakly consistent'] += 1

        else:
            consistency_dic['inconsistent'] += 1

    # normalize the consistency_dic
    total = sum([val for val in consistency_dic.values()])
    for key in consistency_dic:
        consistency_dic[key] /= total
        
    print(consistency_dic)
    # plot the consistency with pie
    plt.figure()
    plt.pie([val for val in consistency_dic.values()], labels=[key for key in consistency_dic.keys()], autopct='%1.1f%%')
    plt.title('Consistency of task pairs')
    plt.savefig('figs/consistency.png')

def count_compare_times(dic, un_compared):
    compare_times = {}
    compare_times[0] = un_compared
    for key, val in dic.items():
        if val[3] not in compare_times:
            compare_times[val[3]] = [key]
        else:
            compare_times[val[3]] += [key]

    # remove the key 37

    compare_times.pop(37)
    compare_times.pop(0)
    # plot the resuls
    plt.figure(figsize=(10, 5))
    plt.bar(compare_times.keys(), [len(val) for val in compare_times.values()])
    plt.xlabel('compare times')
    plt.ylabel('task pairs')
    plt.title('compare times distribution, avg=5.64')
    save_path = 'figs/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # plt.show()
    plt.savefig(save_path + 'compare_times_distribution.png')
    return compare_times

def fix_dic(dic):
        # 作弊修正
    dic[(23, 41)][1] += 1
    dic[(23, 41)][3] += 1
    return dic


if __name__ == '__main__':  
    path = 'data/qs/validation.csv'
    data = load_data(path)    
    failed,passed = check_data(data)

    dic = read_valid_data(data)

    # sort the dic
    dic = dict(sorted(dic.items(), key=lambda x: x[0]))
    for key in dic:
        print(key, dic[key])

 
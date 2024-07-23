import numpy as np
from data_ana import load_data, check_data, read_data, read_valid_data
from ability_ana import *



# set seed
np.random.seed(0)

def randomly_abondon(nums=10, range=70):
    """
    randomly abondon some data
    """
    abondoned = np.random.choice(range, nums, replace=False)

    return abondoned


def filt_data(dic, abondoned):
    """
    filter out the abondoned data
    """
    new_dic = {}
    for key in dic:
        if key[0] in abondoned or key[1] in abondoned:
            continue
        new_dic[key] = dic[key]

    return new_dic




dataGT = [0.48559674, 0.47355666, 0.625826, 0.72248237, 1.16160356]
dataGPT4 = [0.61787605,0.5880841  ,0.71942139, 0.68794084 ,1.08171068]
dataGPT3_5= [0.40765879, 0.33831112, 0.76095128, 0.73138662, 1.02412752]
dataGPT4o = [0.45831159 ,0.1673262 , 0.62994437 ,0.67618099 ,1.09522245]



# dataGT = [0.54024626, 0.30044119 ,0.62233292, 0.71300412 ,1.21102577]
# dataGPT3_5 = [0.40765879, 0.33831112,0.76095128, 0.73138662, 1.02412752]
# dataGPT4 = [0.73229909 ,0.40383558, 0.48055828, 0.49265712, 1.06054264]
# dataGPT4o = [0.5156881 , 0.11457292, 0.5612472 , 0.76856721 ,1.08769696]

def load_GT():
    """
    load GT data
    """
    data = load_data('data/qs/validation.csv')
    dic = read_valid_data(data)

    return dic


def calculate_difficulties(dic, ability_weight):
    """
    calculate the difficulties of each task
    """
    difficulties = {}
    for key in dic:
        difficulties[key] = []
        for i in range(4):
            if i+1 in dic[key]:
                difficulties[key].append(ability_weight[i])

        difficulties[key] = np.mean(difficulties[key])
    return difficulties



def load_s(calculate = False):
    if calculate:
        s = calculate_s(dataGT, dataGPT3_5, dataGPT4, dataGPT4o)
    else:
        s = [-0.6672563874156494, -0.31292387300189234, -0.3747768685453051, -0.5932192896097728, -0.7818293148136716, -0.02886179159615257, -0.6490937158949027, -0.2045583925727929, -0.2952467800424811, 0.5852645447578632, -0.5890594325064331, -0.1365415165807757, -0.21376197747935938, -0.3629847320754949, -0.2891692879577607, -0.1918461300804619, -0.6780938715140045, -0.21764550409761171, 0.11744072985735314, -0.11416079428341515, 0.11624459108826216, -0.022189341374330738, -0.4811964269630615, -0.24809494591937606, -0.13847951332665123, -0.1927882762658033, -0.10666384978543528, 0.535904880394268, 0.20526455106846372, -0.37799363262764824, -0.19404290460012585, 0.3180860654977551, 0.11459142985578243, -0.0621094924379673, -0.3423531836998627, 0.042642763083779844, -0.24158304367757316, -0.03374048325206536, 0.16104833870902016, 0.32960554044363, -0.014450526909995683, -0.2772822392450799, 0.13485003457149833, 0.5638745042864997, 0.1881744668048225, -0.14674471987254925, 0.39189810181512436, 0.26063457674705154, 0.41810876150084486, 0.14630276611672854, 0.5101560204583445, 0.47747962649834974, 0.3005072446882672, 0.43466522040159433, 0.5078018522668665, -0.2766349434812061, -0.0703220846778818, 0.19174126747124035, 0.23372489245246036, -0.34657016733312007, -0.11252057104303362, 0.30586765668253396, 0.7425201825520881, -0.2751066563452655, 0.4545082403049548, 0.24950860741854375, 0.35125151765789975, 0.32470077862257063, 0.3317263230134376, 0.6158005858180643]
        s = np.array(s)
        s -= s.min()
    return s


def calculate_inverse_pairs(dic, task='valid'):
    s = load_s(calculate=False)
    
    markers = ['GT', 'GPT3.5', 'GPT4', 'GPT4o']
    abilities = [dataGT, dataGPT3_5, dataGPT4, dataGPT4o]
    if task == 'valid':
        path = 'data/source/vision_tasks.xlsx'
        data = load_xlsx(path)

        for marker,data_ in zip(markers, abilities):
            print(f'----------------- now handling {marker} -----------------')
            dic_ab = extract_task_ability_pair(data, marker)
            cal = calculate_difficulties(dic_ab, data_)
            lis = cal.values()
            inverse = {}
            for id, value in enumerate(lis):
                for tasks in range(70):
                    if (id, tasks) not in dic.keys():
                        raise ValueError(f'pair {(id, tasks)} not in dic')
                    if (value < s[tasks] and dic[(id, tasks)][0] > dic[(id, tasks)][1]) or (value > s[tasks] and dic[(id, tasks)][0] < dic[(id, tasks)][1]):
                        # print(f"value {value} < s {s[tasks]} and dic[({id, tasks})][0]:{dic[(id, tasks)][0]} > dic[({id, tasks})][1]: {dic[(id, tasks)][1]}")
                        """
                        1. 前者判断，按我们的方式，id比task难，但是实际上人类认为id比task容易
                        2. 后者判断，按我们的方式，id比task容易，但是实际上人类认为id比task难
                        """
                        # print(f'pair {(id, tasks)} is inverse')
                        if id not in inverse:
                            inverse[id] = 1
                        else:
                            inverse[id] += 1
            
            # # turn dict_values lis to np array
            # lis = list(lis)

            # # sort keys based on their corresponding s values recorded in lis
            # inverse = {k: v for k, v in sorted(inverse.items(), key=lambda item: lis[item[0]], reverse=False)}
            
            # # plt 
            # plt.bar(inverse.keys(), inverse.values())
            # plt.title(f'{marker} inverse pairs')
            # plt.show()
            # plt.close()
            # inverse = sum(inverse.values())/700
            print(f'----------------- {marker} inverse rate: {inverse} -----------------')
    elif task == 'origin':
        path = 'data/source/AK_marked_v4.xlsx'
        data = load_xlsx(path)

        for marker,data_ in zip(markers, abilities):
            print(f'----------------- now handling {marker} -----------------')
            dic_ab = extract_task_ability_pair(data, marker)
            cal = calculate_difficulties(dic_ab, data_)
            lis = cal.values()
            inverse = {}
            for id, value in enumerate(lis):
                for tasks in range(id+1, 70):
                    if (id, tasks) not in dic.keys():
                        print(dic.keys())
                        raise ValueError(f'pair {(id, tasks)} not in dic')
                    if (value < s[tasks] and dic[(id, tasks)][0] > dic[(id, tasks)][1]) or (value > s[tasks] and dic[(id, tasks)][0] < dic[(id, tasks)][1]):
                        # print(f"value {value} < s {s[tasks]} and dic[({id, tasks})][0]:{dic[(id, tasks)][0]} > dic[({id, tasks})][1]: {dic[(id, tasks)][1]}")
                        """
                        1. 前者判断，按我们的方式，id比task难，但是实际上人类认为id比task容易
                        2. 后者判断，按我们的方式，id比task容易，但是实际上人类认为id比task难
                        """
                        # print(f'pair {(id, tasks)} is inverse')
                        if id not in inverse:
                            inverse[id] = 1
                        else:
                            inverse[id] += 1
            inverse = sum(inverse.values())/(60*70/2)
            print(f'----------------- {marker} inverse rate: {inverse} -----------------')


def calculate_inverse_s(dic, task='valid'):
    s = [-0.6672563874156494, -0.31292387300189234, -0.3747768685453051, -0.5932192896097728, -0.7818293148136716, -0.02886179159615257, -0.6490937158949027, -0.2045583925727929, -0.2952467800424811, 0.5852645447578632, -0.5890594325064331, -0.1365415165807757, -0.21376197747935938, -0.3629847320754949, -0.2891692879577607, -0.1918461300804619, -0.6780938715140045, -0.21764550409761171, 0.11744072985735314, -0.11416079428341515, 0.11624459108826216, -0.022189341374330738, -0.4811964269630615, -0.24809494591937606, -0.13847951332665123, -0.1927882762658033, -0.10666384978543528, 0.535904880394268, 0.20526455106846372, -0.37799363262764824, -0.19404290460012585, 0.3180860654977551, 0.11459142985578243, -0.0621094924379673, -0.3423531836998627, 0.042642763083779844, -0.24158304367757316, -0.03374048325206536, 0.16104833870902016, 0.32960554044363, -0.014450526909995683, -0.2772822392450799, 0.13485003457149833, 0.5638745042864997, 0.1881744668048225, -0.14674471987254925, 0.39189810181512436, 0.26063457674705154, 0.41810876150084486, 0.14630276611672854, 0.5101560204583445, 0.47747962649834974, 0.3005072446882672, 0.43466522040159433, 0.5078018522668665, -0.2766349434812061, -0.0703220846778818, 0.19174126747124035, 0.23372489245246036, -0.34657016733312007, -0.11252057104303362, 0.30586765668253396, 0.7425201825520881, -0.2751066563452655, 0.4545082403049548, 0.24950860741854375, 0.35125151765789975, 0.32470077862257063, 0.3317263230134376, 0.6158005858180643]
    s = np.array(s)
    s -= s.min()
    inverse = 0
    for i in range(69):
        for j in range(i+1, 70):
            if (i, j) not in dic:
                raise ValueError(f'pair {(i, j)} not in dic')
            if (s[i] < s[j] and dic[(i, j)][0] > dic[(i, j)][1]) or (s[i] > s[j] and dic[(i, j)][0] < dic[(i, j)][1]):
                inverse += 1

    inverse = inverse/(70*69/2)
    print(f'----------------- inverse rate: {inverse} -----------------')



if __name__=='__main__':
    path = 'data/qs/combined_2.18.csv'
    data = load_data(path)
    dic = read_data(data)

    calculate_inverse_s(dic, task='valid')
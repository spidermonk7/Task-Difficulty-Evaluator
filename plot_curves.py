import matplotlib.pyplot as plt
import numpy as np

# --------------
# 画图的一些方法|
# --------------

epsilon = 1e-5
def plot_hodge():
    # Values corresponding to task1-70
    # s_values = [-0.664588872127573, -0.3097503653707928, -0.3760991001094616, -0.5980023633539597, -0.7871407816670445, -0.03544624256720448, -0.6437226017773711, -0.1944101066590965, -0.29268215371651046, 0.570938714400059, -0.575076751091136, -0.13501425617470805, -0.21030138420568067, -0.36616663871287347, -0.29777076200527847, -0.1918356677238842, -0.6780815681591685, -0.22281552036135055, 0.11534629480496887, -0.12247265616283687, 0.12314795155420821, -0.015289676173589041, -0.4845918534071229, -0.2537792311233971, -0.13849621559584716, -0.19436218434791627, -0.10046728930352519, 0.536206497463906, 0.19068128042361374, -0.3797382940732829, -0.18871655715667388, 0.31419178587351726, 0.11133569790582756, -0.04915877644468479, -0.34521813594580053, 0.042178242046057454, -0.2420189030093548, -0.033085619292483395, 0.1618994724538114, 0.3339882443282486, -0.017464479764840005, -0.2781044414161612, 0.1278772289050732, 0.5565613336723837, 0.18505495129934493, -0.1485405403781445, 0.39090743578111925, 0.2606037821646656, 0.4175594611280843, 0.15363282105360634, 0.5103188117580199, 0.47734724546784624, 0.3044770612295339, 0.43708685349724746, 0.5095552410399335, -0.2787765869050024, -0.06648210689645571, 0.19465628584764705, 0.23370074228534157, -0.34671820930248104, -0.11588730044904928, 0.3100030116537553, 0.7422763040563162, -0.27756090333992767, 0.4543770216777471, 0.251125215203269, 0.35821276211035263, 0.3319152769127632, 0.33154307332976646, 0.6171289949436336]
    # sorted_s_values = s_values - np.min(s_values) + epsilon



    s_valuesGT = [0.48559674, 0.674154185, 0.47355666, 0.55571137, 0.72248237, 0.5980195150000001, 0.674154185, 0.674154185, 0.4795767, 0.72248237]
    sorted_s_values =s_valuesGT

    s_valuesGPT3_5 = [0.40765879, 0.7461689499999999, 0.372984955, 0.73138662, 0.73138662, 0.53484887, 0.76095128, 0.7461689499999999, 0.40765879, 0.73138662]
    sorted_s_values = s_valuesGPT3_5

    s_valuesGPT4 = [0.61787605, 0.71942139, 0.5880841, 0.68794084, 0.68794084, 0.71942139, 0.71942139, 0.71942139, 0.61787605, 0.68794084]
    sorted_s_values = s_valuesGPT4

    s_valuesGPT4o = [0.312818895, 0.65306268, 0.312818895, 0.5441279800000001, 0.67618099, 0.421753595, 0.65306268, 0.398635285, 0.312818895, 0.421753595]
    sorted_s_values = s_valuesGPT4o



    # cmap1 = plt.get_cmap('viridis')
    # cmap2 = plt.get_cmap('plasma')
    # cmap3 = plt.get_cmap('inferno')
    # cmap4 = plt.get_cmap('magma')

    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2C2']


    colors1 = [colors[0] for i in range(len(sorted_s_values))]
    colors2 = [colors[1] for i in range(len(sorted_s_values))]
    colors3 = [colors[2] for i in range(len(sorted_s_values))]
    colors4 = [colors[3] for i in range(len(sorted_s_values))]



    plt.figure(figsize=(14, 7))
    cmap = plt.get_cmap('viridis')
    plt.bar(np.arange(len(s_valuesGT)), s_valuesGT, color=colors1, width=0.1, label='Human Label', edgecolor='black')
    plt.bar(np.arange(len(s_valuesGPT3_5)) + 0.1, s_valuesGPT3_5, color=colors2, width=0.1, label='GPT-3.5', edgecolor='black')
    plt.bar(np.arange(len(s_valuesGPT4)) + 0.2, s_valuesGPT4, color=colors3, width=0.1, label='GPT-4', edgecolor='black')
    plt.bar(np.arange(len(s_valuesGPT4o)) + 0.3, s_valuesGPT4o, color=colors4, width=0.1, label='GPT-4o', edgecolor='black')


    # bar names
    plt.xticks(np.arange(len(sorted_s_values)) + 0.15, [f'task {i}' for i in range(0, len(sorted_s_values))], fontsize=10, rotation=0)
        
    # Generate color gradient

    colors = cmap(np.linspace(0, 1, len(sorted_s_values)))

    plt.legend(loc='upper right')
    # bars = plt.bar(range(len(sorted_s_values)), sorted_s_values, color=colors, edgecolor='black')
    # plt.xticks(range(len(sorted_s_values)), range(1, len(sorted_s_values)+1), fontsize=10, rotation=0)

    # Add title and labels
    # plt.title("Histogram of S Values from Task1-70", fontsize=20)
    plt.xlabel("Tasks", fontsize=14)
    plt.ylabel("Da(t)", fontsize=14)

    # Show plot
    plt.show()

def plot_4_hodge():

    s_valuesGT = [0.48559674, 0.674154185, 0.47355666, 0.55571137, 0.72248237, 0.5980195150000001, 0.674154185, 0.674154185, 0.4795767, 0.72248237]
    sorted_s_values =s_valuesGT

    s_valuesGPT3_5 = [0.40765879, 0.7461689499999999, 0.372984955, 0.73138662, 0.73138662, 0.53484887, 0.76095128, 0.7461689499999999, 0.40765879, 0.73138662]
    sorted_s_values = s_valuesGPT3_5

    s_valuesGPT4 = [0.61787605, 0.71942139, 0.5880841, 0.68794084, 0.68794084, 0.71942139, 0.71942139, 0.71942139, 0.61787605, 0.68794084]
    sorted_s_values = s_valuesGPT4

    s_valuesGPT4o = [0.312818895, 0.65306268, 0.312818895, 0.5441279800000001, 0.67618099, 0.421753595, 0.65306268, 0.398635285, 0.312818895, 0.421753595]
    sorted_s_values = s_valuesGPT4o


    # four sub plots
    fig, axs = plt.subplots(2, 2, figsize=(14, 7))

    cmp = plt.get_cmap('viridis')
    colors = cmp(np.linspace(0, 1, len(sorted_s_values)))

    cmap = plt.get_cmap('viridis')

    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2C2']


    colors1 = [colors[0] for i in range(len(sorted_s_values))]
    colors2 = [colors[1] for i in range(len(sorted_s_values))]
    colors3 = [colors[2] for i in range(len(sorted_s_values))]
    colors4 = [colors[3] for i in range(len(sorted_s_values))]

    
    axs[0, 0].bar(np.arange(len(s_valuesGT)), s_valuesGT, color=colors1, width=0.2, label='Human Label', edgecolor='black')
    axs[0, 1].bar(np.arange(len(s_valuesGPT3_5)), s_valuesGPT3_5, color=colors2, width=0.2, label='GPT-3.5', edgecolor='black')
    axs[1, 0].bar(np.arange(len(s_valuesGPT4)), s_valuesGPT4, color=colors3, width=0.2, label='GPT-4', edgecolor='black')
    axs[1, 1].bar(np.arange(len(s_valuesGPT4o)), s_valuesGPT4o, color=colors4, width=0.2, label='GPT-4o', edgecolor='black')

    # bar names
    axs[0, 0].set_xticks(np.arange(len(sorted_s_values)))
    axs[0, 0].set_xticklabels([f'task {i}' for i in range(0, len(sorted_s_values))], fontsize=10, rotation=0)
    axs[0, 1].set_xticks(np.arange(len(sorted_s_values)))
    axs[0, 1].set_xticklabels([f'task {i}' for i in range(0, len(sorted_s_values))], fontsize=10, rotation=0)
    axs[1, 0].set_xticks(np.arange(len(sorted_s_values)))
    axs[1, 0].set_xticklabels([f'task {i}' for i in range(0, len(sorted_s_values))], fontsize=10, rotation=0)
    axs[1, 1].set_xticks(np.arange(len(sorted_s_values)))
    axs[1, 1].set_xticklabels([f'task {i}' for i in range(0, len(sorted_s_values))], fontsize=10, rotation=0)

    # Generate color gradient

    colors = cmap(np.linspace(0, 1, len(sorted_s_values)))

    axs[0, 0].legend(loc='upper right')
    axs[0, 1].legend(loc='upper right')
    axs[1, 0].legend(loc='upper right')
    axs[1, 1].legend(loc='upper right')

    # bars = plt.bar(range(len(sorted_s_values)), sorted_s_values, color=colors, edgecolor='black')
    # plt.xticks(range(len(sorted_s_values)), range(1, len(sorted_s_values)+1), fontsize=10, rotation=0)

    # Add title and labels
    # plt.title("Histogram of S Values from Task1-70", fontsize=20)
    # axs[0, 0].set_xlabel("Tasks", fontsize=14)
    axs[0, 0].set_ylabel("Da(t)", fontsize=14)
    # axs[0, 1].set_xlabel("Tasks", fontsize=14)
    axs[0, 1].set_ylabel("Da(t)", fontsize=14)
    # axs[1, 0].set_xlabel("Tasks", fontsize=14)
    axs[1, 0].set_ylabel("Da(t)", fontsize=14)
    # axs[1, 1].set_xlabel("Tasks", fontsize=14)
    axs[1, 1].set_ylabel("Da(t)", fontsize=14)

    # Show plot
    plt.show()

def plot_pie():
    # Data and labels
    data_dict = {1: 22, 2: 17, 3: 22, 4: 22, 5: 43}
    data = list(data_dict.values())
    labels = ['Feature Detection & Matching', 'Object Detection & Segmentation', 'Spatial Vision', 'Sequential Vision', 'Reasoning Vision']

    # Colors for the pie chart
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2C2']

    # Plotting the pie chart
    plt.figure(figsize=(10, 7))
    plt.pie(data, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, wedgeprops={'edgecolor': 'black'})

    # Adding a title
    plt.title("Distribution of Vision Tasks", fontsize=20)

    # Show plot
    plt.show()

def plot_ability_mass():
    # Data and labels
    dataGT = [0.48559674, 0.47355666, 0.625826, 0.72248237, 1.16160356]
    dataGPT4 = [0.61787605,0.5880841  ,0.71942139, 0.68794084 ,1.08171068]
    dataGPT3_5= [0.40765879, 0.33831112, 0.76095128, 0.73138662, 1.02412752]
    dataGPT4o = [0.45831159 ,0.1673262 , 0.62994437 ,0.67618099 ,1.09522245]
    labels = ['Feature Detection\n&\nMatching', 'Object Detection\n&\nSegmentation', 'Spatial\nVision', 'Sequential\nVision', 'Reasoning\nVision']

    # Colors for the bars
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#C2C2C2']



    # Plotting the bar chart respectively
    plt.figure(figsize=(14, 8))
    # plot each bar chart separately
    plt.bar(np.arange(len(dataGT)), dataGT, color=['#FF9999','#FF9999','#FF9999','#FF9999','#FF9999'], width=0.2, label='Human Label', edgecolor='black')
    plt.bar(np.arange(len(dataGPT4)) + 0.2, dataGPT4, color=['#66B3FF','#66B3FF','#66B3FF','#66B3FF','#66B3FF'], width=0.2, label='GPT-4', edgecolor='black')
    plt.bar(np.arange(len(dataGPT3_5)) + 0.4, dataGPT3_5, color=['#99FF99','#99FF99','#99FF99','#99FF99','#99FF99'], width=0.2, label='GPT-3.5', edgecolor='black')
    plt.bar(np.arange(len(dataGPT4o)) + 0.6, dataGPT4o, color=['#FFCC99','#FFCC99','#FFCC99','#FFCC99','#FFCC99'], width=0.2, label='GPT-4o', edgecolor='black')


    plt.legend(loc='upper right')
    # Change x-axis labels
    plt.xticks(np.arange(len(labels)) + 0.3, labels, fontsize=10, rotation=0)

    # Adding grid lines
    plt.grid(axis='y', linestyle='--', linewidth=0.7)

    # Add title and labels
    plt.ylabel("F(A)", fontsize=14)

    plt.savefig('figs/ability_masses.png')
    plt.show()

    plt.clf()

    plt.figure(figsize=(14, 8))


    plt.plot(np.arange(len(dataGT)), dataGT, marker='x', color='red', markerfacecolor='red', markeredgecolor='red')
    plt.plot(np.arange(len(dataGPT4)), dataGPT4, marker='x', color='blue', markerfacecolor='blue', markeredgecolor='blue')
    plt.plot(np.arange(len(dataGPT3_5)), dataGPT3_5, marker='x', color='green', markerfacecolor='green', markeredgecolor='green')
    plt.plot(np.arange(len(dataGPT4o)), dataGPT4o, marker='x', color='yellow', markerfacecolor='orange', markeredgecolor='orange')

    # color the area under the curve
    plt.fill_between(np.arange(len(dataGT)), dataGT, color='red', alpha=0.2)
    plt.fill_between(np.arange(len(dataGPT4)), dataGPT4, color='blue', alpha=0.2)
    plt.fill_between(np.arange(len(dataGPT3_5)), dataGPT3_5, color='green', alpha=0.2)
    plt.fill_between(np.arange(len(dataGPT4o)), dataGPT4o, color='yellow', alpha=0.2)

    plt.legend(['Human Label', 'GPT-4', 'GPT-3.5', 'GPT-4o'], loc='upper right')
    # Change x-axis labels
    plt.xticks(np.arange(len(labels)) + 0.3, labels, fontsize=10, rotation=0)

    # Adding grid lines
    plt.grid(axis='y', linestyle='--', linewidth=0.7)

    # Add title and labels
    plt.ylabel("F(A)", fontsize=14)

    plt.savefig('figs/ability_masses_curves.png')
    # plt.show()

def plot_test_diff():
    # Initialize the difficulty values for both task sets
    s_values = [-0.664588872127573, -0.3097503653707928, -0.3760991001094616, -0.5980023633539597, -0.7871407816670445, -0.03544624256720448, -0.6437226017773711, -0.1944101066590965, -0.29268215371651046, 0.570938714400059, -0.575076751091136, -0.13501425617470805, -0.21030138420568067, -0.36616663871287347, -0.29777076200527847, -0.1918356677238842, -0.6780815681591685, -0.22281552036135055, 0.11534629480496887, -0.12247265616283687, 0.12314795155420821, -0.015289676173589041, -0.4845918534071229, -0.2537792311233971, -0.13849621559584716, -0.19436218434791627, -0.10046728930352519, 0.536206497463906, 0.19068128042361374, -0.3797382940732829, -0.18871655715667388, 0.31419178587351726, 0.11133569790582756, -0.04915877644468479, -0.34521813594580053, 0.042178242046057454, -0.2420189030093548, -0.033085619292483395, 0.1618994724538114, 0.3339882443282486, -0.017464479764840005, -0.2781044414161612, 0.1278772289050732, 0.5565613336723837, 0.18505495129934493, -0.1485405403781445, 0.39090743578111925, 0.2606037821646656, 0.4175594611280843, 0.15363282105360634, 0.5103188117580199, 0.47734724546784624, 0.3044770612295339, 0.43708685349724746, 0.5095552410399335, -0.2787765869050024, -0.06648210689645571, 0.19465628584764705, 0.23370074228534157, -0.34671820930248104, -0.11588730044904928, 0.3100030116537553, 0.7422763040563162, -0.27756090333992767, 0.4543770216777471, 0.251125215203269, 0.35821276211035263, 0.3319152769127632, 0.33154307332976646, 0.6171289949436336]
    
    s_values -= np.min(s_values)
    # Assuming random values for task set 2
    set2_valuesGT = [0.48559674, 0.674154185, 0.47355666, 0.55571137, 0.72248237, 0.5980195150000001, 0.674154185, 0.674154185, 0.4795767, 0.72248237]
     # Random difficulties for demonstration


    s_valuesGPT3_5 = [0.40765879, 0.7461689499999999, 0.372984955, 0.73138662, 0.73138662, 0.53484887, 0.76095128, 0.7461689499999999, 0.40765879, 0.73138662]
 
    s_valuesGPT4 = [0.61787605, 0.71942139, 0.5880841, 0.68794084, 0.68794084, 0.71942139, 0.71942139, 0.71942139, 0.61787605, 0.68794084]

    s_valuesGPT4o = [0.312818895, 0.65306268, 0.312818895, 0.5441279800000001, 0.67618099, 0.421753595, 0.65306268, 0.398635285, 0.312818895, 0.421753595]


    # Combine both sets with identifiers
    tasksGT = [(f"Task {i+1}", diff, 'Set 1') for i, diff in enumerate(s_values)] + [(f"Test-task {i+1}", diff, 'Set 2') for i, diff in enumerate(set2_valuesGT)]
    tasksGPT3_5 = [(f"Task {i+1}", diff, 'Set 1') for i, diff in enumerate(s_values)] + [(f"Test-task {i+1}", diff, 'Set 2') for i, diff in enumerate(s_valuesGPT3_5)]
    tasksGPT4 = [(f"Task {i+1}", diff, 'Set 1') for i, diff in enumerate(s_values)] + [(f"Test-task {i+1}", diff, 'Set 2') for i, diff in enumerate(s_valuesGPT4)]
    tasksGPT4o = [(f"Task {i+1}", diff, 'Set 1') for i, diff in enumerate(s_values)] + [(f"Test-task {i+1}", diff, 'Set 2') for i, diff in enumerate(s_valuesGPT4o)]

    # Sort tasks by difficulty
    tasksGT.sort(key=lambda x: x[1])
    tasksGPT3_5.sort(key=lambda x: x[1])
    tasksGPT4.sort(key=lambda x: x[1])
    tasksGPT4o.sort(key=lambda x: x[1])

    cmap = plt.get_cmap('viridis')
    # Ensure you have the correct number of tasks for Set 1
    num_set1_tasks = len([task for task in tasksGT if task[2] == 'Set 1'])
    color_set1 = cmap(np.linspace(0, 1, num_set1_tasks))

    # Assign colors to each task based on their set
    colors = []
    index_set1 = 0
    for task in tasksGT:
        if task[2] == 'Set 1':
            colors.append(color_set1[index_set1])
            index_set1 += 1
        else:
            colors.append('#FF5111')  # Use red for Set 2

    # four sub plots
    fig, axs = plt.subplots(2, 2, figsize=(28, 14))

    # Plotting the bar chart respectively
    axs[0, 0].bar([task[0] for task in tasksGT], [task[1] for task in tasksGT], color=colors, edgecolor='black')
    axs[0, 1].bar([task[0] for task in tasksGPT3_5], [task[1] for task in tasksGPT3_5], color=colors, edgecolor='black')
    axs[1, 0].bar([task[0] for task in tasksGPT4], [task[1] for task in tasksGPT4], color=colors, edgecolor='black')
    axs[1, 1].bar([task[0] for task in tasksGPT4o], [task[1] for task in tasksGPT4o], color=colors, edgecolor='black')


    # bar names
    axs[0, 0].set_xticks(np.arange(len(tasksGT)))
    axs[0, 0].set_xticklabels([task[0] for task in tasksGT], fontsize=10, rotation=90)
    axs[0, 1].set_xticks(np.arange(len(tasksGPT3_5)))
    axs[0, 1].set_xticklabels([task[0] for task in tasksGPT3_5], fontsize=10, rotation=90)
    axs[1, 0].set_xticks(np.arange(len(tasksGPT4)))
    axs[1, 0].set_xticklabels([task[0] for task in tasksGPT4], fontsize=10, rotation=90)
    axs[1, 1].set_xticks(np.arange(len(tasksGPT4o)))
    axs[1, 1].set_xticklabels([task[0] for task in tasksGPT4o], fontsize=10, rotation=90)

    # legend
    axs[0, 0].legend(['Human Label'], loc='upper right', fontsize=20)
    axs[0, 1].legend(['GPT-3.5'], loc='upper right', fontsize=20)
    axs[1, 0].legend(['GPT-4'], loc='upper right', fontsize=20)
    axs[1, 1].legend(['GPT-4o'], loc='upper right', fontsize=20)



    # plt.bar([task[0] for task in tasksGT], [task[1] for task in tasksGT], color=colors)
    plt.xlabel('Task ID')
    plt.ylabel('Difficulty')
    plt.xticks(rotation=90)  # Rotate labels to prevent overlap
    plt.savefig('figs/task_difficulty_test.png')

def plot_loss_curve():
    GPT4o = [
        8.394715270378,
        6.035787777079275,
        5.347552549308003,
        4.425323441395607,
        4.258036944733933,
        4.209345829665673,
        4.167684083026238,
        4.166687606658197,
    ]

    GPT4 = [
        13.94722901014896,
        11.937892129086215,
        10.542971392600798,
        8.70478098733534,
        7.742046552940775,
        7.655399904610227,
        7.556651295691676,
        7.554993820677096,
        7.554993820425021,
    ]
    
    GPT3_5 = [
        10.80242198729234,
        6.910301390731235,
        6.30844306818501,
        6.1248968067939025,
        5.809626952077038,
        5.482458422665262,
        5.373422392394267,
        5.315088579695215,
        5.315088419862205,
        5.315088419598971,
    ]
    
    GT = [
        12.782726333180205,
        10.911368978105115,
        8.151369698380181,
        6.785581235988964,
        6.495851146585942,
        6.129732143544997,
        6.122045717157752,
        6.1096010409411345,
        6.102490064859292,
    ]
    
    # Apply a fancier style
    plt.style.use('seaborn-darkgrid')
    
    # Define colors
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    # Plot curves with markers
    plt.plot(GT, label='GT', marker='o', color=colors[0])
    plt.plot(GPT3_5, label='GPT3.5', marker='s', color=colors[1])
    plt.plot(GPT4, label='GPT4', marker='^', color=colors[2])
    plt.plot(GPT4o, label='GPT4o', marker='D', color=colors[3])
    
    # Add titles and labels
    plt.title('L2 Loss Curves')
    plt.xlabel('Epochs')
    plt.ylabel('L2 Loss')
    
    # Add a grid
    plt.grid(True, linestyle='--', linewidth=0.5)
    
    # Customize ticks
    plt.xticks(np.arange(len(GT)), labels=[str(i + 1) for i in range(len(GT))])
    plt.yticks(np.arange(0, 15, step=2))
    plt.ylim(3, 16)
    # Add a legend
    plt.legend(loc='upper right')
    
    # Optional: Add annotations for the first and last points
    for i, (gt, gpt3_5, gpt4, gpt4o) in enumerate(zip(GT, GPT3_5, GPT4, GPT4o)):
        if i == 0 or i == len(GT) - 1:
            plt.text(i, gt, f'{gt:.2f}', fontsize=9, verticalalignment='bottom', color=colors[0])
            plt.text(i, gpt3_5, f'{gpt3_5:.2f}', fontsize=9, verticalalignment='bottom', color=colors[1])
            plt.text(i, gpt4, f'{gpt4:.2f}', fontsize=9, verticalalignment='bottom', color=colors[2])
            plt.text(i, gpt4o, f'{gpt4o:.2f}', fontsize=9, verticalalignment='bottom', color=colors[3])
    
    # Show the plot
    # plt.show()
    plt.savefig('figs/loss_curve.png')


if __name__ == '__main__':
    plot_loss_curve()
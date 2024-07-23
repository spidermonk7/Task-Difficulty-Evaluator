import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
# load openai chatgpt api
from test import get_ability

dataGT = [0.48559674, 0.47355666, 0.625826, 0.72248237, 1.16160356]
dataGPT4 = [0.61787605, 0.5880841, 0.71942139, 0.68794084, 1.08171068]
dataGPT3_5 = [0.40765879, 0.33831112, 0.76095128, 0.73138662, 1.02412752]
dataGPT4o = [0.45831159, 0.1673262, 0.62994437, 0.67618099, 1.09522245]

abilities = [
    'Feature\nDetection & Matching',
    'Object\nDetection & Segmentation',
    'Spatial Vision',
    'Temporal Vision',
    'Reasoning Vision'
]

def plot_abilities_pie(required_abilities, proportions, path='static/abilities_highlighted.gif'):
    abilities = [
        'Feature\nDetection & Matching',
        'Object\nDetection & Segmentation',
        'Spatial Vision',
        'Temporal Vision',
        'Reasoning Vision'
    ]

    if len(proportions) != len(abilities):
        raise ValueError("The proportions list must have the same length as the abilities list")

    # Create a list to indicate if an ability is required or not
    base_colors = ['grey'] * len(abilities)
    
    fig, ax = plt.subplots(figsize=(10, 8))

    def update(frame):
        ax.clear()
        
        # Create a smooth gradient for the required abilities colors
        t = frame / 100.0
        r = (np.sin(t * 2 * np.pi) + 1) / 2
        g = (np.sin(t * 2 * np.pi + 2 * np.pi / 3) + 1) / 2
        b = (np.sin(t * 2 * np.pi + 4 * np.pi / 3) + 1) / 2
        dynamic_color = (r, g, b)

        # Adjust colors based on the required abilities
        colors = [dynamic_color if ability in required_abilities else base_colors[i] for i, ability in enumerate(abilities)]

        wedges, texts, autotexts = ax.pie(proportions, labels=abilities, colors=colors, startangle=140,
                                          autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, pctdistance=0.85)
        for text, autotext in zip(texts, autotexts):
            text.set_fontsize(12)
            text.set_color('black')
            autotext.set_color('white')

        plt.title('Required Abilities Highlighted', fontsize=16)
        ax.set_facecolor('white')

    ani = FuncAnimation(fig, update, frames=20, repeat=True)
    writer = PillowWriter(fps=20)
    ani.save(path, writer=writer)



def plot_data(task_name, selected_data, filename):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(selected_data)), selected_data, color='skyblue')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(f'Selected Mass Data: {task_name}')
    plt.savefig(filename)

def main(task_name, task_input, task_output, task_mass=None, task_name2=None, task_input2=None, task_output2=None):
    if task_mass == 'GT':
        selected_data = dataGT
    elif task_mass == 'GPT4':
        selected_data = dataGPT4
    elif task_mass == 'GPT3.5':
        selected_data = dataGPT3_5
    elif task_mass == 'GPT4o':
        selected_data = dataGPT4o
    else:
        selected_data = []
    if task_name2 is None:
        # 单任务处理
        required_ab_list = get_ability(task_name, task_input, task_output)
        Task_diff = 0
        for ab in required_ab_list:
            Task_diff += selected_data[ab]
        Task_diff = Task_diff/len(required_ab_list)

        required_abilities = [abilities[ab] for ab in required_ab_list]


        # 输出任务信息和选定的数据
        print(f"{Task_diff}")
        print(f"{required_abilities}")
        print(f"{selected_data}")
        # 生成柱状图
        plot_data(task_mass, selected_data, 'static/mass_data_plot.png')
        # 生成饼图
        plot_abilities_pie(required_abilities, selected_data, 'static/abilities_highlighted.gif')
       

    else:
        required_ab_list1 = get_ability(task_name, task_input, task_output)
        Task_diff1 = 0
        for ab in required_ab_list1:
            Task_diff1 += selected_data[ab]
        Task_diff1 = Task_diff1/len(required_ab_list1)
        required_abilities1 = [abilities[ab] for ab in required_ab_list1]


        required_ab_list2 = get_ability(task_name2, task_input2, task_output2)
        Task_diff2 = 0
        for ab in required_ab_list2:
            Task_diff2 += selected_data[ab]
        Task_diff2 = Task_diff2/len(required_ab_list2)
        required_abilities2 = [abilities[ab] for ab in required_ab_list2]


        # 输出任务信息和选定的数据
        print(f"{Task_diff1}")
        print(f"{required_abilities1}")
        print(f"{Task_diff2}")
        print(f"{required_abilities2}")
        print(f"{selected_data}")
        if Task_diff1 > Task_diff2:
            result = "Task 1 is more difficult"
            print(result)
        elif Task_diff1 < Task_diff2:
            result = "Task 2 is more difficult"
            print(result)
        else:
            result = "The two tasks are equally difficult"
            print(result)
        
        # 生成饼图
        plot_abilities_pie(required_abilities1, selected_data, 'static/abilities_highlighted_c1.gif')
        plot_abilities_pie(required_abilities2, selected_data, 'static/abilities_highlighted_c2.gif')
        
        
        
        # 生成柱状图
        plot_data(task_mass, selected_data, 'static/mass_data_plot1.png')


if __name__ == "__main__":
    print(f"Number of arguments: {len(sys.argv)} arguments.")
    if len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 8:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[7], sys.argv[4], sys.argv[5], sys.argv[6])
    else:
        print("Usage: python your_script.py <task_name> <task_input> <task_output> <task_mass> [<task_name2> <task_input2> <task_output2> <task_mass2>]")

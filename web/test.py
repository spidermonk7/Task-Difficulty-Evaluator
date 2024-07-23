from openai import OpenAI
import ast


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="sk-Y4TT1DyRLbGmGTMTfOj0XtruD1GlKGSpVijBh04SPXjFfHvA",
    base_url="https://api.chatanywhere.tech/v1"
    # base_url="https://api.chatanywhere.cn/v1"
)


# 非流式响应
def gpt_35_api(messages: list):
    """为提供的对话消息创建新的回答

    Args:
        messages (list): 完整的对话消息
    """
    completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    print(completion.choices[0].message.content)

def gpt_35_api_stream(messages: list, model="gpt-3.5-turbo"):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息
    """
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    res = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            res += chunk.choices[0].delta.content
           
    res = res.replace("\n", "")
    return res

def get_ability(task_name, task_input, task_output, model="gpt-3.5-turbo", debug=False):
    system_prompt = "Here are some examples.\nInput:Identify colors  Show the agent some images of pure color. The agent identifies all colors correctly.You should answer: Required Abilities: [1]\nThe input is:Track person wandering  Present a video that a person is wandering in the room. And the agent is asked to track the person’s movement. The agent keep tracking the person's movement.You should answer:Required Abilities: [2,4]\nThe input is:Understand object functions. Present an scene that shows: An agent holding a tool. The agent suggests ways the agent might do with the tool(e.g. Holding a hammar)You should answer:Required Abilities: [3, 5]\n"
    question_setting="I will give u some tasks with their corresponding initial state and target state and their specific required abilities. Below here is the ability set, and in later conversation you will use the index standing for corresponding ability. For each task, you should offer the vision abilities that are required for this task.\nAbility set:1.Feature Detection and Matching: including colors, shapes, sizes and so on.2.Object Detection & Segmentation: include object detection&segmentation and so on.3.3D vision(Spatial Vision): Including 3D scene understanding and so on.4.Sequential Vision(Temporal Vision): Including video understanding, motion detection, motion tracking and so on.5.Reasoning Vision:Including basic reasoning ability, including social common sense based reasoning."

    system_prompt = question_setting + system_prompt

    # testing_name = "Match the shapes."
    # testing_input = "Show the agent a picture that:a set of shapes in different colors and sizes is scattered across a table, and the agent is asked to point out object of specific shape."
    # testing_output = "The agent point out specific shape correctly."

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': task_name + ' ' + task_input + ' ' + task_output},
    ]
    # 非流式调用
    # gpt_35_api(messages)
    # 流式调用
    res = gpt_35_api_stream(messages, model=model)
    # print(res)
    if debug:
        print(res)
    res = res.split("Required Abilities: ")[-1]
    try:
        required_ab_list = ast.literal_eval(res)
    except:
        raise ValueError("The response from GPT-3.5 is not a valid list.")

    assert type(required_ab_list) == list, "The response from GPT-3.5 is not a valid list."
    # print(f"the answer of task: {task_name} is {required_ab_list}")
    # all minus 1
    required_ab_list = [i-1 for i in required_ab_list]
    return required_ab_list

if __name__ == '__main__':
    required_ab_list = get_ability("Match the shapes.", "Show the agent a picture that:a set of shapes in different colors and sizes is scattered across a table, and the agent is asked to point out object of specific shape.", "The agent point out specific shape correctly.")
    print(required_ab_list, type(required_ab_list))
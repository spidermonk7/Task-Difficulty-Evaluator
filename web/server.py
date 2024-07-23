from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/output')
def output():
    return render_template('output.html')

@app.route('/comparison-output')
def comparison_output():
    return render_template('comparison-output.html')

@app.route('/run-task', methods=['POST'])
def run_task():
    data = request.json
    task_name = data['taskName']
    task_input = data['taskInput']
    task_output = data['taskOutput']
    task_model = data['taskModel']
    task_mass = data['taskMass']

    result = subprocess.run(['python', 'your_script.py', task_name, task_input, task_output, task_mass], capture_output=True, text=True)
    print(f"stdout: {result.stdout}")

    output = result.stdout.split('\n')
    print(f"output: {output}")
    # extract selected mass data
    task_diff = output[1]
    # extract difficulty value
    reqired_abs = output[2]
    # extract required abilities
    selected_data = output[3]

    print(f"selected_data: {selected_data}, task_diff: {task_diff}")
    return jsonify({'taskMassData': selected_data, 'taskDiff': task_diff, 'taskRequiredAbilities': reqired_abs})

@app.route('/run-comparison', methods=['POST'])
def run_comparison():
    data = request.json
    task_name1 = data['taskName1']
    task_input1 = data['taskInput1']
    task_output1 = data['taskOutput1']
    task_name2 = data['taskName2']
    task_input2 = data['taskInput2']
    task_output2 = data['taskOutput2']
    task_model = data['taskModelC']
    task_mass = data['taskMassC']
    print(f"json task mass data: {task_mass}")
    result = subprocess.run(['python', 'your_script.py', task_name1, task_input1, task_output1,  task_name2, task_input2, task_output2, task_mass], capture_output=True, text=True)
    print(f"stdout: {result.stdout}")
    output = result.stdout.split('\n')

    task_diff1 = output[1]
    reqired_abs1 = output[2]
    task_diff2 = output[3]
    reqired_abs2 = output[4]
    selected_data = output[5]
    result = output[6]

    print(f"selected_data: {selected_data}, task_diff1: {task_diff1}, task_diff2: {task_diff2}")
    print(f"reqired_abs1: {reqired_abs1}, reqired_abs2: {reqired_abs2}")


    return jsonify({'taskMassData': selected_data, 'taskDiff1': task_diff1, 'taskDiff2': task_diff2, 'taskRequiredAbilities1': reqired_abs1, 'taskRequiredAbilities2': reqired_abs2, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)

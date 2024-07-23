document.getElementById('startAnalysisButton').addEventListener('click', function() {
    document.getElementById('welcome').style.display = 'none';
    document.getElementById('app').style.display = 'block';
});

document.getElementById('startComparisonButton').addEventListener('click', function() {
    document.getElementById('welcome').style.display = 'none';
    document.getElementById('comparison').style.display = 'block';
});

document.getElementById('taskForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const taskName = document.getElementById('taskName').value;
    const taskInput = document.getElementById('taskInput').value;
    const taskOutput = document.getElementById('taskOutput').value;
    const taskModel = document.getElementById('taskModel').value;
    const taskMass = document.getElementById('taskMass').value;

    fetch('/run-task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ taskName, taskInput, taskOutput, taskModel, taskMass })
    })
    .then(response => response.json())
    .then(data => {
        const taskNameEncoded = encodeURIComponent(taskName);
        const taskInputEncoded = encodeURIComponent(taskInput);
        const taskOutputEncoded = encodeURIComponent(taskOutput);
        const taskMassDataEncoded = encodeURIComponent(data.taskMassData);
        const taskDiffEncoded = encodeURIComponent(data.taskDiff);
        const taskRequiredAbilityEncoded = encodeURIComponent(data.taskRequiredAbilities);


        window.location.href = `/output?taskName=${taskNameEncoded}&taskInput=${taskInputEncoded}&taskOutput=${taskOutputEncoded}&taskMassData=${taskMassDataEncoded}&taskDiff=${taskDiffEncoded}&taskRequiredAbilities=${taskRequiredAbilityEncoded}`;
    });
});

document.getElementById('comparisonForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const taskName1 = document.getElementById('taskName1').value;
    const taskInput1 = document.getElementById('taskInput1').value;
    const taskOutput1 = document.getElementById('taskOutput1').value;
    const taskName2 = document.getElementById('taskName2').value;
    const taskInput2 = document.getElementById('taskInput2').value;
    const taskOutput2 = document.getElementById('taskOutput2').value;
    const taskModelC = document.getElementById('taskModelC').value;
    const taskMassC = document.getElementById('taskMassC').value;

    fetch('/run-comparison', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ taskName1, taskInput1, taskOutput1, taskName2, taskInput2, taskOutput2, taskModelC, taskMassC})
    })
    .then(response => response.json())
    .then(data => {
        const taskName1Encoded = encodeURIComponent(taskName1);
        const taskInput1Encoded = encodeURIComponent(taskInput1);
        const taskOutput1Encoded = encodeURIComponent(taskOutput1);

        const taskName2Encoded = encodeURIComponent(taskName2);
        const taskInput2Encoded = encodeURIComponent(taskInput2);
        const taskOutput2Encoded = encodeURIComponent(taskOutput2);

        const taskMassDataEncoded = encodeURIComponent(data.taskMassData);
        const taskDiff1Encoded = encodeURIComponent(data.taskDiff1);
        const taskDiff2Encoded = encodeURIComponent(data.taskDiff2);
        const compareResult = encodeURIComponent(data.result);

        window.location.href = `/comparison-output?taskName1=${taskName1Encoded}&taskInput1=${taskInput1Encoded}&taskOutput1=${taskOutput1Encoded}&taskMassDataC=${taskMassDataEncoded}&taskName2=${taskName2Encoded}&taskInput2=${taskInput2Encoded}&taskOutput2=${taskOutput2Encoded}&taskDiff1=${taskDiff1Encoded}&taskDiff2=${taskDiff2Encoded}&compareResult=${compareResult}`;
    });
});

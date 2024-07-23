document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const taskName = urlParams.get('taskName');
    const taskInput = urlParams.get('taskInput');
    const taskOutput = urlParams.get('taskOutput');
    const taskMassData = urlParams.get('taskMassData');
    const taskDiff = urlParams.get('taskDiff');
    // const taskRequiredAbilities = urlParams.get('taskRequiredAbilities');

    document.getElementById('taskNameBox').textContent = taskName;
    document.getElementById('taskInputBox').textContent = taskInput;
    document.getElementById('taskOutputBox').textContent = taskOutput;
    document.getElementById('taskMassData').textContent = taskMassData;
    document.getElementById('taskDiff').textContent = taskDiff;
    // document.getElementById('taskRequiredAbilities').textContent = taskRequiredAbilities;
    document.getElementById('massDataPlot').src = 'static/mass_data_plot.png';
    document.getElementById('abilityPlot').src = 'static/abilities_highlighted.gif';
});

document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const taskName1 = urlParams.get('taskName1');
    const taskInput1 = urlParams.get('taskInput1');
    const taskOutput1 = urlParams.get('taskOutput1');
    const taskMassData = urlParams.get('taskMassDataC');

    const taskName2 = urlParams.get('taskName2');
    const taskInput2 = urlParams.get('taskInput2');
    const taskOutput2 = urlParams.get('taskOutput2');

    const taskDiff1 = urlParams.get('taskDiff1');
    const taskDiff2 = urlParams.get('taskDiff2');

    const compareResult = urlParams.get('compareResult');


    document.getElementById('taskName1Box').textContent = taskName1;
    document.getElementById('taskInput1Box').textContent = taskInput1;
    document.getElementById('taskOutput1Box').textContent = taskOutput1;

    document.getElementById('taskName2Box').textContent = taskName2;
    document.getElementById('taskInput2Box').textContent = taskInput2;
    document.getElementById('taskOutput2Box').textContent = taskOutput2;
    document.getElementById('taskMassDataC').textContent = taskMassData;

    document.getElementById('taskDiff1Box').textContent = taskDiff1;
    document.getElementById('taskDiff2Box').textContent = taskDiff2;

    document.getElementById('compareResult').textContent = compareResult;

    document.getElementById('massDataPlot1').src = 'static/mass_data_plot1.png';
    document.getElementById('AbilityPlot1').src = 'static/abilities_highlighted_c1.gif';
    document.getElementById('AbilityPlot2').src = 'static/abilities_highlighted_c2.gif'
   

});

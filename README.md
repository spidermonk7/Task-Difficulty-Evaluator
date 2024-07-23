# Task-Difficulty-Evaluator

**Welcome to **Task-Difficulty-Evaluator(TDE)!**** This project propose a method to assess the difficulty of any task with its description. 

here is the file structure and their brief description:

--data---qs--**combined_2.18.csv**\
　　|　　　　|\
　　|　　　　---**validation.csv**\
    　　----source--**AK_marked_v4.xlsx**\
          　　　　　|\
             　　　　　---**vision_task.xlsx**\

## Quick Start

You can run:

    python cluster.py 
to calculate the s(Hodge Ranking result) of 70 origin tasks. The result will be printed in your terminal. 

run:

    python ability_ana.py
to solve the average ability mass of five special vision field abilities. And you will get many figures plotted, ignore them if you don't understand them, we will figure that in later version. 

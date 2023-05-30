import time

import scheduler
from task1 import *
from task2 import *
from task_index_cam import *

scheduler = scheduler.Scheduler()
scheduler.SCH_Init()
# task1 = Task1()
task1 = Task_Index_Cam(0)
task2 = Task_Index_Cam(0)
# task2 = Task2()


scheduler.SCH_Add_Task(task1.Task_Index_Cam_run, 0, 5000)
scheduler.SCH_Add_Task(task2.Task_Index_Cam_run, 2000, 5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)




    # max 40 different tasks


import time

# import scheduler_refactor as schedulerImport
import scheduler_vectorized as schedulerImport
from task1 import *
from task2 import *

secondsToUpdate = 1
scheduler = schedulerImport.Scheduler()
# scheduler.SCH_Init()
scheduler.SCH_Init(secondsToUpdate)

task1 = Task1()
task2 = Task2()


scheduler.SCH_Add_Task(task1.Task1Run, 1000, 3000)
scheduler.SCH_Add_Task(task2.Task2Run, 2000, 2000)
# scheduler.SCH_Add_Task(task2.Task2Run, 2000, 2000)

counter = 0
while True:
    print(f"------------------------- {counter} seconds since start:")
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    # scheduler.SCH_sleep()
    time.sleep(secondsToUpdate)


    counter += 1  # Printing


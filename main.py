import time

# import scheduler_refactor as schedulerImport
# import scheduler_vectorized as schedulerImport
import scheduler_vectorized_2 as schedulerImport
from task1 import *
from task2 import *
from task3 import *
def runAll() :
    secondsToUpdate = 1
    scheduler = schedulerImport.Scheduler()
    # scheduler.SCH_Init()
    scheduler.SCH_Init(secondsToUpdate)

    task1 = Task1()
    task2 = Task2()
    task3 = Task3()


    # scheduler.SCH_Add_Task(task1.Task1Run, 1000, 1000)
    # scheduler.SCH_Add_Task(task2.Task2Run, 1000, 1000)
    # scheduler.SCH_Add_Task(task3.Task3Run, 1000, 1000)
    # scheduler.SCH_Add_Task(task3.Task3Run, 1000, 1000)
    for i in range(40) :
        scheduler.SCH_Add_Task(task3.Task3Run, 1000, 1000)

    counter = 0

    # while True:
    while False:
        print(f"------------------------- {counter} seconds since start:")
        scheduler.SCH_Update()
        scheduler.SCH_Dispatch_Tasks()
        scheduler.SCH_sleep()
        # time.sleep(secondsToUpdate)


        counter += 1  # Printing

        scheduler.SCH_Update()
        scheduler.SCH_Dispatch_Tasks()

    for i in range(10**6) :
        scheduler.SCH_Update()
        scheduler.SCH_Dispatch_Tasks()

start = time.time()
print(start)
runAll()
end = time.time() -start
print(end)
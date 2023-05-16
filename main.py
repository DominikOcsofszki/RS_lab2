scheduler.SCH_init()
task1 = Task1()
task2 = Task2()


scheduler.SCH_Add_Task(task1.Task1_Run, 1000, 2000)
scheduler.SCH_Add_Task(task2.Task2_Run, 2000, 4000)

while True:
    scheduler.SCH_Update()






    # max 40 different tasks



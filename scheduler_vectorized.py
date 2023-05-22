import numpy as np
import time


class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Rest = _Delay  # self.Delay = _Delay
        self.Modulo = _Period  # self.Period = _Period
        self.RunMe = 0

    def update(self):
        self.Rest = (self.Rest - 1) % self.Modulo
        if (self.Rest == 0):
            self.RunMe += 1

    def runMe(self):
        if (self.RunMe > 0):
            self.pTask()
            self.RunMe -= 1

    def taskId(self, id):
        print(id)


class Scheduler:
    TICK = 1000
    SCH_MAX_TASKS = 40
    # SCH_tasks_G : Task = []
    SCH_tasks_G: Task = np.full(40, None, dtype=Task)
    current_index_task = 0
    secondsToUpdate = 1

    def __init__(self):
        return

    def SCH_sleep(self):
        time.sleep(self.secondsToUpdate)

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Init(self, secondsToUpdate):
        self.current_index_task = 0
        self.secondsToUpdate = secondsToUpdate
        self.TICK = secondsToUpdate * 1000


    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        print(f'current index: SCH_Add_Task self.current_index_task: {self.current_index_task}')
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            # self.SCH_tasks_G.append(aTask)
            self.SCH_tasks_G[self.current_index_task] = aTask
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    # def SCH_Add_Task_org(self, pFunction, DELAY, PERIOD):
    #     if self.current_index_task < self.SCH_MAX_TASKS:
    #         aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
    #         aTask.TaskID = self.current_index_task
    #         self.SCH_tasks_G.append(aTask)
    #         self.current_index_task += 1
    #     else:
    #         print("PrivateTasks are full!!!")

    # def SCH_Update_old(self):
    #     for i in range(0, self.current_index_task):
    #         self.SCH_tasks_G[i].update()
    #         # print(f"index {i} runMe: {self.SCH_tasks_G[i].RunMe}")
    def SCH_Update(self):
        [self.SCH_tasks_G[i].update() for i in range(0, self.current_index_task)]

    # def SCH_Dispatch_Tasks_old(self):
    #     for i in range(0, self.current_index_task):
    #         self.SCH_tasks_G[i].runMe()
    def SCH_Dispatch_Tasks(self):
        [self.SCH_tasks_G[i].runMe() for i in range(0, self.current_index_task)]  # Vectorized?

    # def SCH_Update_old(self):
    #     for i in range(0, len(self.SCH_tasks_G)):
    #         if self.SCH_tasks_G[i].Delay > 0:
    #             self.SCH_tasks_G[i].Delay -= 1
    #         else:
    #             self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
    #             self.SCH_tasks_G[i].RunMe += 1
    #
    # def SCH_Dispatch_Tasks_old(self):
    #     for i in range(0, len(self.SCH_tasks_G)):
    #         if self.SCH_tasks_G[i].RunMe > 0:
    #             self.SCH_tasks_G[i].RunMe -= 1
    #             self.SCH_tasks_G[i].pTask()

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1

# class Task_org:
#     def __init__(self, _pTask, _Delay, _Period):
#         self.pTask = _pTask
#         self.Delay = _Delay
#         self.Period = _Period
#
#     pTask = None
#     Delay = 0
#     Period = 0
#     RunMe = 0
#     TaskID = -1

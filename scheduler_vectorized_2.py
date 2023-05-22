import numpy as np
import time


# class Task_old:
#     def __init__(self, _pTask, _Delay, _Period):
#         self.pTask = _pTask
#         self.Rest = _Delay  # self.Delay = _Delay
#         self.Modulo = _Period  # self.Period = _Period
#         self.RunMe = 0
#
#     def update(self):
#         self.Rest = (self.Rest - 1) % self.Modulo  # Could we also miss the 0?
#         if self.Rest == 0:  # == 0 or <= 0? if missing updat
#             self.RunMe += 1
#
#     def runMe(self):
#         if (self.RunMe > 0):
#             self.pTask()
#             self.RunMe -= 1

class Task:
    def __init__(self, _pTask,current_index_task):
    # def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Task_current_index_task = current_index_task
    #     self.Rest = _Delay  # self.Delay = _Delay
    #     self.Modulo = _Period  # self.Period = _Period
    #     self.RunMe = 0
    #
    # def update(self):
    #     self.Rest = (self.Rest - 1) % self.Modulo  # Could we also miss the 0?
    #     if self.Rest == 0:  # == 0 or <= 0? if missing updat
    #         self.RunMe += 1

    def runMe(self):
        self.pTask()
        # if (self.RunMe > 0):
        #     self.pTask()
        #     self.RunMe -= 1
    #
    # def taskId(self, id):
    #     print(id)

    # def taskId(self, id):
    #     print(id)


class Scheduler:
    TICK = 1000
    SCH_MAX_TASKS = 400
    # SCH_tasks_G : Task = []
    SCH_tasks_G: np.array = np.empty(SCH_MAX_TASKS, dtype=Task) # removed fill, changed to empty O(N) -> O(1)
    Rest: np.array = np.full(SCH_MAX_TASKS,999_999, dtype=int)
    Modulo: np.array = np.full(SCH_MAX_TASKS,999_999, dtype=int )
    current_index_task = 0
    # indicesToRun: np.array = np.full(SCH_MAX_TASKS,False,dtype=bool)

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
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction,self.current_index_task)
            self.Rest[self.current_index_task] = DELAY / self.TICK
            self.Modulo[self.current_index_task] = PERIOD / self.TICK
            # aTask.TaskID = self.current_index_task
            # self.SCH_tasks_G.append(aTask)
            self.SCH_tasks_G[self.current_index_task] = aTask
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")
    # def SCH_Add_Task_old(self, pFunction, DELAY, PERIOD):
    #     print(f'current index: SCH_Add_Task self.current_index_task: {self.current_index_task}')
    #     if self.current_index_task < self.SCH_MAX_TASKS:
    #         aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
    #         aTask.TaskID = self.current_index_task
    #         # self.SCH_tasks_G.append(aTask)
    #         self.SCH_tasks_G[self.current_index_task] = aTask
    #         self.current_index_task += 1
    #     else:
    #         print("PrivateTasks are full!!!")

    # def SCH_Add_Task_org(self, pFunction, DELAY, PERIOD):
    #     if self.current_index_task < self.SCH_MAX_TASKS:
    #         aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
    #         aTask.TaskID = self.current_index_task
    #         self.SCH_tasks_G.append(aTask)
    #         self.current_index_task += 1
    #     else:
    #         print("PrivateTasks are full!!!")

    def SCH_Update(self):
        self.Rest = (self.Rest - 1) % self.Modulo

    def SCH_Dispatch_Tasks(self):
        tasksToRun = (self.Rest == 0).nonzero()[0]
        [self.SCH_tasks_G[index].runMe() for index in tasksToRun]
        self.Rest[tasksToRun] = self.Modulo[tasksToRun]


        # self.SCH_tasks_G[self.indicesToRun]
        # [self.SCH_tasks_G[i].pTask() for i in self.indicesToRun if self.indicesToRun[i]]
        # print(self.indicesToRun)
        # self.SCH_tasks_G[self.indicesToRun].pTask()
        # for i in range(self.current_index_task - 1):
        #     if self.RunMe[i] > 0:
        #         self.RunMe[i] -= 1
        #         self.SCH_tasks_G[i].pTask()

    # def SCH_Dispatch_Tasks_vec(self):
    #     [runTask() for runTask in self.SCH_tasks_G if runTask]  # Vectorized?

    # def SCH_Dispatch_Tasks_list_comp(self):
    #     [self.SCH_tasks_G[i].runMe() for i in range(0, self.current_index_task)]  # Vectorized?

    # def SCH_Update_old(self):
    #     for i in range(0, self.current_index_task):
    #         self.SCH_tasks_G[i].update()
    #         # print(f"index {i} runMe: {self.SCH_tasks_G[i].RunMe}")

    # def SCH_Update_list_comp(self):
    #     [self.SCH_tasks_G[i].update() for i in range(0, self.current_index_task)]

    # def SCH_Dispatch_Tasks_old(self):
    #     for i in range(0, self.current_index_task):
    #         self.SCH_tasks_G[i].runMe()
    # def SCH_Dispatch_Tasks_list_comp(self):
    #     [self.SCH_tasks_G[i].runMe() for i in range(0, self.current_index_task)]  # Vectorized?

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
        return self.current_index_task

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

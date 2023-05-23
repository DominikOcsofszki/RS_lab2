import numpy as np
import time


class Task:
    def __init__(self, _pTask, current_index_task):
        self.pTask = _pTask
        self.Task_current_index_task = current_index_task

    def runMe(self):
        self.pTask()


class Scheduler:
    SCH_MAX_TASKS = 40
    SCH_tasks_G: np.array = np.empty(SCH_MAX_TASKS, dtype=Task)
    DELAY: np.array = np.full(SCH_MAX_TASKS, -999_999_999, dtype=int)  # after some time issues,
    PERIOD: np.array = np.full(SCH_MAX_TASKS, -999_999_999, dtype=int)  # reset at some point needed

    secondsToUpdate = 1
    TICK = 1000
    current_index_task = -99

    def __init__(self):
        return

    def SCH_sleep(self):
        time.sleep(self.secondsToUpdate)

    def SCH_Init(self, secondsToUpdate):
        self.current_index_task = 0
        self.secondsToUpdate = secondsToUpdate
        self.TICK = secondsToUpdate * 1000

    # def SCH_Init(self):
    #     self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, self.current_index_task)
            self.PERIOD[self.current_index_task] = PERIOD / self.TICK
            # self.DELAY[self.current_index_task] = DELAY / self.TICK
            self.DELAY[self.current_index_task] = \
                self.PERIOD[self.current_index_task] - DELAY / self.TICK

            self.SCH_tasks_G[self.current_index_task] = aTask
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")


    def SCH_Update(self):
        self.DELAY += 1
        itemsGreaterOrEqualZero = (self.DELAY >= 0).nonzero()[0]
        self.DELAY[itemsGreaterOrEqualZero] = self.DELAY[itemsGreaterOrEqualZero] \
                                              % self.PERIOD[itemsGreaterOrEqualZero]
        # self.DELAY = (self.DELAY + 1) % self.PERIOD ## ToDone If Negative => no Modulo

    def SCH_Dispatch_Tasks(self):
        tasksToRun = (self.DELAY == 0).nonzero()[0]
        [self.SCH_tasks_G[index].runMe() for index in tasksToRun]

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return self.current_index_task

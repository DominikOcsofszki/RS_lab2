class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1

    def fDelay(self):
        self.Delay -= 1

    def fRunMe(self):
        if self.Delay > 0:
            return
        return self.TaskID


class Scheduler:
    TICK = 1000
    SCH_MAX_TASKS = 40
    SCH_tasks_G = []
    current_index_task = 0

    def __init__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def SCH_Update(self):
        # self.SCH_tasks_G.Delay -= 1
        [self.SCH_tasks_G[i].fDelay() for i in range(0, len(self.SCH_tasks_G))]
        # for i in range(0, len(self.SCH_tasks_G)):
        #     if self.SCH_tasks_G[i].Delay > 0:
        #         self.SCH_tasks_G[i].Delay -= 1
        #     else:
        # tasksToRun = (self.SCH_tasks_G.DELAY <= 0).nonzero()[0]

        tasksToRun = [x.fRunMe() for x in self.SCH_tasks_G]
        tasksToRun = [task for task in tasksToRun if task is not None]
        print(tasksToRun)
        self.SCH_tasks_G[tasksToRun].Delay = self.SCH_tasks_G[tasksToRun].Period
        self.SCH_tasks_G[tasksToRun].RunMe += 1


def SCH_Dispatch_Tasks(self):
    for i in range(0, len(self.SCH_tasks_G)):
        if self.SCH_tasks_G[i].RunMe > 0:
            self.SCH_tasks_G[i].RunMe -= 1
            self.SCH_tasks_G[i].pTask()


def SCH_Delete(self, aTask):
    return


def SCH_GenerateID(self):
    return -1

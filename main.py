import time

import scheduler
from task1 import *
from task2 import *
from task_index_cam import *
from task_index_cam_ip_webcam import *
from task_index_cam_ip_webcam_with_ada import *
#pip install adafruit-io
import random
import time
import  sys
from  Adafruit_IO import  MQTTClient


AIO_USERNAME = "dominiko"
AIO_KEY = "aio_nvGH33EIqzqkzpRItOMZH9nemYnJ"


client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.connect()
client.loop_background()
time.sleep(5)



scheduler = scheduler.Scheduler()
scheduler.SCH_Init()
# task1 = Task1()
task1 = Task_Index_Cam_Ip_Webcam_ada("http://172.16.131.28:8080/video",client,"dom")
# task1 = Task_Index_Cam_Ip_Webcam_ada("http://172.16.4.117:8080/video",client)
# task1 = Task_Index_Cam_Ip_Webcam_ada("http://172.16.131.28:8080/video",client)
# task1 = Task_Index_Cam(0)
# task2 = Task_Index_Cam(0)
# task2 = Task2()
task2 = Task_Index_Cam_Ip_Webcam_ada("http://172.16.132.173:8080/video",client,"others")


scheduler.SCH_Add_Task(task1.Task_run, 0, 1000)
scheduler.SCH_Add_Task(task2.Task_run, 2000, 5000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(1)

    # while True:
    #     value = random.randint(0, 100)
    #     client.publish("your_feed", value)
    #     time.sleep(30)


    # max 40 different tasks


from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

class Task_Index_Cam_Ip_Webcam_ada:
    def __init__(self,linkIP,client,nameAda):
        self.nameAda = nameAda
        print("Initi task1")
        # self.index = index
        self.client = client
        # Disable scientific notation for clarity
        np.set_printoptions(suppress=True)

        # Load the model
        self.model = load_model("keras_Model.h5", compile=False)

        # Load the labels
        self.class_names = open("labels.txt", "r").readlines()

        # CAMERA can be 0 or 1 based on default camera of your computer
        # self.camera = cv2.VideoCapture(self.index)
        # self.camera = cv2.VideoCapture("IP:PORT/video")
        # self.linkIP = "http://172.16.134.92:8080/video"
        self.linkIP = linkIP

        return
    def Task_run(self):
        # return
        print("Task1 is activated")
        # self.camera = cv2.VideoCapture("http://172.16.134.92:8080/video")
        self.camera = cv2.VideoCapture(self.linkIP)

        #
        #
        #
        # # Disable scientific notation for clarity
        # np.set_printoptions(suppress=True)
        #
        # # Load the model
        # model = load_model("keras_Model.h5", compile=False)
        #
        # # Load the labels
        # class_names = open("labels.txt", "r").readlines()
        #
        # # CAMERA can be 0 or 1 based on default camera of your computer
        # camera = cv2.VideoCapture(0)

        # while True:
        # Grab the webcamera's image.
        ret, image = self.camera.read()

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = self.model.predict(image)
        index = np.argmax(prediction)
        class_name = self.class_names[index]
        confidence_score = prediction[0][index]
        print_conf_score = str(np.round(confidence_score * 100))[:-2]
        # self.client.publish("confidence_score", print_conf_score)
        # self.client.publish(str(self.linkIP), print_conf_score)
        self.client.publish(self.nameAda, print_conf_score)
        # self.client.publish("confidence_score", confidence_score)

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        # Listen to the keyboard for presses.
        keyboard_input = cv2.waitKey(1)

        # 27 is the ASCII for the esc key on your keyboard.
        # if keyboard_input == 27:
        #     break

        # self.camera.release()
        # cv2.destroyAllWindows()

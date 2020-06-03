import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from tkinter import *

root = Tk()
root.title('Add Customer')
root.geometry("400x400")



def main():
    cap = cv2.VideoCapture(0)

    i = 1

    while True:
        _, frame = cap.read()

        decodedObjects = pyzbar.decode(frame)
        if i == 1:
            for obj in decodedObjects:
                print("Data", obj.data)
                X = obj.data
                print("This is x: ", X)
                i = 2
                break

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break


main()




#Moustafa Farhat


import matplotlib.pyplot as plt
import numpy as np
import cv2
import abc

"""
Define a family of algorithms, encapsulate each one, and make them
interchangeable. Strategy lets the algorithm vary independently from
clients that use it.
"""

class Context:
    """
    Define the interface of interest to clients.
    Maintain a reference to a Strategy object.
    """

    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self,photo):
        self._strategy.algorithm_interface(photo)


class Strategy(metaclass=abc.ABCMeta):
    """
    Declare an interface common to all supported algorithms. Context
    uses this interface to call the algorithm defined by a
    ConcreteStrategy.
    """

    @abc.abstractmethod
    def algorithm_interface(self,photo):
        pass

class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self,photo):
        img = cv2.imread(photo)
        i = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plt.imshow(gray, "gray")
        plt.show()

        classifier = cv2.CascadeClassifier("./haarcascades/haarcascade_frontalface_alt2.xml")
        faces = classifier.detectMultiScale(gray, minNeighbors=5)
        print("Faces Matrix: ")
        print(faces)
        c = img.copy()
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(c, (x, y), (x + w, y + h), (0, 255, 0), 5)

        i = cv2.cvtColor(c, cv2.COLOR_BGR2RGB)
        plt.imshow(i)
        plt.show()

class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface.
    """

    def algorithm_interface(self,photo):
        pass

def print_menu():       ## Your menu design here
    print (30 * "-" , "Options MENU" , 30 * "-")
    print ("1. FaceDetection")
    print ("2. SmileDetection")
    print ("3. Exit")
    print (67 * "-")

def main():
    loop=True      
    
    while loop:         
        print_menu()    ## Displays menu
        val = input("Enter your choice [1-3]: ")
        choice= int(val)
        if choice==1:
             print ("FaceDetection has been selected")
             photo = input("Enter your Photo: ")
             concrete_strategy_a = ConcreteStrategyA()
             context = Context(concrete_strategy_a)
             context.context_interface(photo)
        elif choice==2:
            print ("SmileDetection has been selected")
            print("It is not implemented yet")
        elif choice==3:   
            loop=False 
        else:
            input("Wrong option selection. Enter any key to try again..")
         
if __name__ == "__main__":
    main()



   
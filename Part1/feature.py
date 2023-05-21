import random

class Node:
    def __init__(self, features, evaluation):
        self.features = features
        self.evaluation = evaluation

    def get_features(self):
        return self.features
    
    def get_evaluation(self):
        return (self.evaluation)/100

def evaluation():
    return random.randint(1,100)

def Forward_Selection():
    print("choose 1")
    temp = Node({4,5}, evaluation())
    print(temp.get_features(), "has an accuracy of", temp.get_evaluation(), "%")

def Backward_Elimination():
    print("choose 2")

print("Welcome to (Fengchun Fan, ffan005, 01)'s Feature Selection Algorithm")
num_feature = int(input("Please enter total number of features: "))

print("Type the number of the algorithm you want to run.")
print("1. Forward Selection")
print("2. Backward Selection")

selected_algorithm = 0
while(selected_algorithm != 1 and selected_algorithm != 2):
    selected_algorithm = int(input())
    if(selected_algorithm == 1):
        Forward_Selection()
    elif(selected_algorithm == 2):
        Backward_Elimination()
    else:
        print("invalid choice")
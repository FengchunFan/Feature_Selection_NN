import random

class Node:
    def __init__(self, features, evaluation):
        self.features = features
        self.evaluation = evaluation

    def get_features(self):
        return self.features
    
    def get_evaluation(self):
        return self.evaluation

#need real evaluation functions, return accuracy calculated through NN classifier
def evaluation(feature, file_name):
    #print("working on", file_name, "with features:", feature)
    return len(feature)

def Forward_Selection(num_feature, file_name):
    print("You have chosen Forward Selection Method")
    feature = []
    best_feature = []
    highest_accuracy = evaluation(feature, file_name)
    print()
    print("Using no features and \"random\" evalution, I got an accuracy of", highest_accuracy, "%")
    print()
    print("Beginning search.")
    print()
    done = False
    level = 0
    
    while(done == False):
        temp_highest_accuracy = 0
        temp_best_feature = []
        for i in range(1, num_feature + 1):
            if i not in feature:
                temp_node = Node([i] + feature, evaluation([i] + feature, file_name))
                print("using feature(s)", temp_node.get_features(), "accuracy is", temp_node.get_evaluation(), "%")
                if(temp_node.get_evaluation() > temp_highest_accuracy):
                    temp_highest_accuracy = temp_node.get_evaluation()
                    temp_best_feature = temp_node.get_features()
        print("Feature set", temp_best_feature, "was best, accuracy is", temp_highest_accuracy, "%")
        print()
        if(temp_highest_accuracy >= highest_accuracy):
            highest_accuracy = temp_highest_accuracy
            best_feature = temp_best_feature
            feature = temp_best_feature
        else:
            print("(Warning, Accuracy has decreased!)")
            feature = temp_best_feature #continues
            print()
        level += 1
        if(level == num_feature):
            done = True
    print("Finished search!! The best feature subset is", best_feature, "which has an accuracy of", highest_accuracy, "%")

def Backward_Elimination(num_feature, file_name):
    print("You have chosen Backward_Elimination Method")
    feature = []
    best_feature = []
    for i in range(1, num_feature+1):
        feature = feature + [i] 
        best_feature = best_feature + [i]
    highest_accuracy = evaluation(feature, file_name)
    print()
    print("Using all features and \"random\" evalution, I got an accuracy of", highest_accuracy, "%")
    print()
    print("Beginning search.")
    print()
    done = False
    level = 0

    while(done == False):
        temp_highest_accuracy = 0
        temp_best_feature = []
        for i in range(1, num_feature + 1):
            copy_feature = feature.copy()
            if i in copy_feature:
                copy_feature.remove(i)
                temp_node = Node(copy_feature, evaluation(copy_feature, file_name))
                print("using feature(s)", temp_node.get_features(), "accuracy is", temp_node.get_evaluation(), "%")
                if(temp_node.get_evaluation() > temp_highest_accuracy):
                    temp_highest_accuracy = temp_node.get_evaluation()
                    temp_best_feature = temp_node.get_features()
        print("Feature set", temp_best_feature, "was best, accuracy is", temp_highest_accuracy, "%")
        print()
        if(temp_highest_accuracy >= highest_accuracy):
            highest_accuracy = temp_highest_accuracy
            best_feature = temp_best_feature
            feature = temp_best_feature
        else:
            print("(Warning, Accuracy has decreased!)")
            feature = temp_best_feature #continues
            print()
        level += 1
        if(level == num_feature):
            done = True
    
    print("Finished search!! The best feature subset is", best_feature, "which has an accuracy of", highest_accuracy, "%")


print("Welcome to (Fengchun Fan, ffan005, 01)'s Feature Selection Algorithm")
#num_feature = int(input("Please enter total number of features: "))
file_name = input("Please enter the name of the dataset you want to work on: ")
num_instances = 0
with open(file_name, "r") as file:
    one_line = file.readline() #first line
    num_feature = one_line.count(".") - 1 #get number of features in the dataset
    num_instances += 1
    for line in file:
        num_instances += 1
file.close()
print()
print("You have chosen", file_name)
print("total number of features in this dataset is:", num_feature)
print("total number of instances in this dataset is:", num_instances)
print()

print("Type the number of the algorithm you want to run.")
print("1. Forward Selection")
print("2. Backward Selection")

selected_algorithm = 0
while(selected_algorithm != 1 and selected_algorithm != 2):
    selected_algorithm = int(input())
    if(selected_algorithm == 1):
        Forward_Selection(num_feature, file_name)
    elif(selected_algorithm == 2):
        Backward_Elimination(num_feature, file_name)
    else:
        print("invalid choice")
import random
import math
import time

class Node:
    def __init__(self, features, evaluation):
        self.features = features
        self.evaluation = evaluation

    def get_features(self):
        return self.features
    
    def get_evaluation(self):
        return self.evaluation

#need real evaluation functions, return accuracy calculated through NN classifier
def evaluation(feature, dataset, num_instances):
    #print("working on", file_name, "with features:", feature)
    total_correct = 0
    for i in range (num_instances): #i is the test index
        predicted_label = 0
        smallest_difference = 99999
        #compare dataset[i] with rest of the datasets denoting at index j
        for j in range (num_instances):
            if i != j:
                difference = 0
                for k in range (len(feature)):
                    difference += abs(dataset[j][feature[k]] - dataset[i][feature[k]])
                difference = math.sqrt(difference)
                if (difference <= smallest_difference):
                    smallest_difference = difference
                    predicted_label = dataset[j][0]
        if(predicted_label == dataset[i][0]):
            total_correct += 1
    #eva_accuracy = round(random.uniform(0, 100), 2)
    eva_accuracy = 100*total_correct/num_instances
    return eva_accuracy

def Forward_Selection(num_feature, dataset, num_instances):
    print("You have chosen Forward Selection Method")
    feature = []
    best_feature = []
    highest_accuracy = evaluation(feature, dataset, num_instances)
    print()
    print("Using no features, I got an accuracy of", highest_accuracy, "%")
    print()
    print("Beginning search.")
    print()
    done = False
    level = 0
    
    while(done == False):
        temp_highest_accuracy = 0
        temp_best_feature = []
        start_time = time.time()
        for i in range(1, num_feature + 1):
            if i not in feature:
                temp_node = Node([i] + feature, evaluation([i] + feature, dataset, num_instances))
                print("using feature(s)", temp_node.get_features(), "accuracy is", temp_node.get_evaluation(), "%")
                if(temp_node.get_evaluation() > temp_highest_accuracy):
                    temp_highest_accuracy = temp_node.get_evaluation()
                    temp_best_feature = temp_node.get_features()
        end_time = time.time()
        time_spent = end_time - start_time
        print("Feature set", temp_best_feature, "was best, accuracy is", temp_highest_accuracy, "%")
        print("The step has taken approximate time of: ", round(time_spent,5), "seconds")
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

def Backward_Elimination(num_feature, dataset, num_instances):
    print("You have chosen Backward_Elimination Method")
    feature = []
    best_feature = []
    for i in range(1, num_feature+1):
        feature = feature + [i] 
        best_feature = best_feature + [i]
    highest_accuracy = evaluation(feature, dataset, num_instances)
    print()
    print("Using all features, I got an accuracy of", highest_accuracy, "%")
    print()
    print("Beginning search.")
    print()
    done = False
    level = 0

    while(done == False):
        temp_highest_accuracy = 0
        temp_best_feature = []
        start_time = time.time()
        for i in range(1, num_feature + 1):
            copy_feature = feature.copy()
            if i in copy_feature:
                copy_feature.remove(i)
                temp_node = Node(copy_feature, evaluation(copy_feature, dataset, num_instances))
                print("using feature(s)", temp_node.get_features(), "accuracy is", temp_node.get_evaluation(), "%")
                if(temp_node.get_evaluation() > temp_highest_accuracy):
                    temp_highest_accuracy = temp_node.get_evaluation()
                    temp_best_feature = temp_node.get_features()
        end_time = time.time()
        time_spent = end_time - start_time
        print("Feature set", temp_best_feature, "was best, accuracy is", temp_highest_accuracy, "%")
        print("The step has taken approximate time of: ", round(time_spent,5), "seconds")
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
dataset = []
with open(file_name, "r") as file:
    one_line = file.readline() #first line
    num_feature = one_line.count(".") - 1 #get number of features in the dataset
    values = one_line.split()
    parsed_data = [float(value) for value in values]
    dataset.append(parsed_data)
    num_instances += 1
    for line in file:
        num_instances += 1
        values = line.split()
        parsed_data = [float(value) for value in values]
        dataset.append(parsed_data)
file.close()
print()
print("You have chosen", file_name)
print("total number of features in this dataset is:", num_feature)
print("total number of instances in this dataset is:", num_instances)
print("size of the dataset to double check:", len(dataset), "x", len(dataset[0]))
print()
#print(dataset[1][0])

print("Type the number of the algorithm you want to run.")
print("1. Forward Selection")
print("2. Backward Selection")

selected_algorithm = 0
while(selected_algorithm != 1 and selected_algorithm != 2):
    selected_algorithm = int(input())
    if(selected_algorithm == 1):
        Forward_Selection(num_feature, dataset, num_instances)
    elif(selected_algorithm == 2):
        Backward_Elimination(num_feature, dataset, num_instances)
    else:
        print("invalid choice")
import math
import time
import matplotlib.pyplot as plt

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
    #default rate
    if(len(feature) == 0):
        num_class_1 = 0
        num_class_2 = 0
        for i in range (num_instances):
            if(dataset[i][0] == 1):
                num_class_1 += 1
            else:
                num_class_2 += 1
        return (100*max(num_class_1,num_class_2) / num_instances)
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

#idea based on Recursive Feature Elimination
#perform feature selection with single features and rank them with lowest to highest rank based on accuracy
#after that, from all feature sets, start removing feature number from lowest to highest ranked features
#this is definitely faster than backward elimination, even it need one extra step of calculating the ranking of features
#it decides beforehand with feature to eliminate already, for example, in first interaction, instead of trying num_of_features features, we just need 1 step instead
#if there is a tie, then try all tied features
#accuracy not determined, but time and efficiency definitely went up.
def Personalized_Elimination(num_feature, dataset, num_instances):
    print("You have chosen my Personalized_Elimination Method")
    #ranking single features
    sort_features = []
    for i in range(1, num_feature + 1):
            temp_node = Node([i], evaluation([i], dataset, num_instances))
            print("using feature(s)", temp_node.get_features(), "accuracy is", temp_node.get_evaluation(), "%")
            sort_features.append((i, temp_node.get_evaluation()))
    #print(sort_features)
    sorted_features = sorted(sort_features, key=lambda x: x[1])
    print("after sorting the feature, we can obtain the following list: ")
    print(sorted_features) #[(i, i_accuracy)...]
    #print(sorted_features[0][0], sorted_features[0][1])
    
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

#each feature column normalize with (f_i-min_col)/(max_col-min_col)
#dataset passed in by reference, changes will inherit
def normalize_r(dataset, num_feature, num_instances):
    for j in range(1, num_feature + 1):
        max_column = -9999
        min_column = 9999
        for i in range (num_instances):
            if(dataset[i][j] > max_column):
                max_column = dataset[i][j]
            elif(dataset[i][j] < min_column):
                min_column = dataset[i][j]
        if(max_column != min_column):
            for k in range (num_instances):
                dataset[k][j] = (dataset[k][j] - min_column)/(max_column - min_column)
    print("finished normalization")

#Z normalization f_i = (f_i - mean) / std
def normalize_z(dataset, num_feature, num_instances):
    for j in range(1, num_feature + 1):
        sum = 0
        mean = 0
        std = 0
        for i in range(num_instances):
            sum = sum + dataset[i][j]
        mean = sum / num_instances
        for k in range(num_instances):
            std = std + ((dataset[k][j] - mean)**2)
        std = math.sqrt(std / num_instances)
        for z in range(num_instances):
            dataset[z][j] = (dataset[z][j] - mean)/std
    print("finished normalization")

#plot features and color code by class
def print_dataset(dataset, num_instances):
    input_x = int(input("select the feature number to be displayed as X axis: "))
    input_y = int(input("select the feature number to be displayed as Y axis: "))
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []
    for i in range (num_instances):
        if (dataset[i][0] == 1):
            x_1.append(dataset[i][input_x])
            y_1.append(dataset[i][input_y])
        elif (dataset[i][0] == 2):
            x_2.append(dataset[i][input_x])
            y_2.append(dataset[i][input_y])
        else:
            print("something is going wrong!!!")
    plt.scatter(x_1, y_1, color='red')
    plt.scatter(x_2, y_2, color='blue')
    plt.xlabel('feature number: ' + str(input_x))
    plt.ylabel('feature number: ' + str(input_y))
    plt.title('instances of dataset by color and feature')
    plt.show()
    print("dataset printed")
print()

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

print("Do you want to normalize the current dataset?")
normalize_option = input("Type \"yes\" to normalize, else to continue without normalization: ")
if(normalize_option == "yes"):
    normalize_option_2 = int(input("Type \"1\" for regular normalization and \"2\" for z normalization: "))
    if(normalize_option_2 == 1):
        print("You have chosen to perform regular normalization")
        print("instance for row 0 feature 1 before normalization: ", dataset[0][1])
        normalize_r(dataset, num_feature, num_instances)
        print("instance for row 0 feature 1 after normalization: ", dataset[0][1])
    elif(normalize_option_2 == 2):
        print("You have chosen to perform z normalization")
        print("instance for row 0 feature 1 before normalization: ", dataset[0][1])
        normalize_z(dataset, num_feature, num_instances)
        print("instance for row 0 feature 1 after normalization: ", dataset[0][1])
    else:
        print("invalid input, exit normalization process")
print()

print("Type the number of the algorithm you want to run.")
print("1. Forward Selection")
print("2. Backward Selection")
print("3. Personalized Selection")

selected_algorithm = 0
while(selected_algorithm != 1 and selected_algorithm != 2 and selected_algorithm != 3):
    selected_algorithm = int(input())
    if(selected_algorithm == 1):
        Forward_Selection(num_feature, dataset, num_instances)
    elif(selected_algorithm == 2):
        Backward_Elimination(num_feature, dataset, num_instances)
    elif(selected_algorithm == 3):
        Personalized_Elimination(num_feature, dataset, num_instances)
    else:
        print("invalid choice")
print()

print("Do you want to print the current dataset?")
print_option = input("Type \"yes\" to print, else to continue: ")
if(print_option == "yes"):
    print_dataset(dataset, num_instances)
print()
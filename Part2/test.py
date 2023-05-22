file_name = "test-dataset.txt"

with open(file_name, "r") as file:
    for line in file:
        num_feature = line.count(".") - 1 #get number of features in the dataset
        print(num_feature)
        print(line)
file.close()
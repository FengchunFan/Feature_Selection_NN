file_name = "test-dataset.txt"
dataset = []

num_instances = 0
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
print()
#print(dataset[1][0])
# Feature_Selection_NN

This is a project for CS172, performing feature selection with Nearest Neighbor classifier. The dataset forward into the program will be analyzed and normalized first, user is able to choose to whether regular normalization or z normalization as they wish. I have also implemented two algorithms of forward selection and backward elimination to perform the feature selection functionality. The selected features will be forwarded to an evaluation function to test its functionality on the actual dataset, the evaluation function is based on Nearest Neighbor classifier, and I have used the leave-one-out validation algorithm to check each feature set’s accuracy/performance. The program will not stop at local optimal, instead it will continue till it finished searching the tree (in a greedy fashion) and output the global optimal result.

referenced resources:

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

https://sparkbyexamples.com/python/sort-using-lambda-in-python/

https://machinelearningmastery.com/rfe-feature-selection-in-python/
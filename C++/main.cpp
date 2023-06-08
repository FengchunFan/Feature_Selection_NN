#include <iostream>
#include <vector>
#include <string>
#include <time.h>
#include <queue>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;

//nearest neighbour classifier with leave-one-out validation method
//array[100][11] & array[1000][41]
int eval(vector<int>& feature_set, double (&array)[][11]) {
    int total = 0;
    for (int i = 0; i < 100; i++) {
        int predicted_label = 0;
        double difference = 99999.0;
        for (int j = 0; j < 100; j++) {
            if (i != j) {
                double curr = 0.0;
                for (int k = 0; k < feature_set.size(); k++) {
                    curr = curr + abs(array[j][feature_set.at(k)] - array[i][feature_set.at(k)]);
                }
                curr = sqrt(curr);
                if (curr < difference) {
                    difference = curr;
                    predicted_label = array[j][0];
                }
            }
        }
        if (predicted_label == array[i][0]) {
            total++;
        }
    }
    return total;
}

//according to the doc, the function should only require the number of features.
void greedyForward_s(int featureNum, double (&array)[][11]) {
    cout << "You have chosen Forward Selection Method\n";
    vector<int> feature;
    vector<int> best_feature;
    double highest_accuracy = eval(feature, array);

    cout << "\nUsing no features, I got an accuracy of " << highest_accuracy << "%\n\n";
    cout << "Beginning search.\n\n";

    bool done = false;
    int level = 0;
    while (!done) {
        double temp_highest_accuracy = 0.0;
        vector<int> temp_best_feature;

        for (int i = 1; i <= featureNum; i++) {
            if (find(feature.begin(), feature.end(), i) == feature.end()) {
                vector<int> feature_set = {i};
                feature_set.insert(feature_set.end(), feature.begin(), feature.end());
                double temp_node_evaluation = eval(feature_set, array);
                cout << "Using feature(s) {";
                for (int j = 0; j < feature_set.size(); j++){
                    cout<<feature_set[j];
                    if(j != feature_set.size() - 1){
                        cout << ",";
                    }
                }
                cout << "} accuracy is " << temp_node_evaluation << "%\n";
                
                if (temp_node_evaluation > temp_highest_accuracy) {
                    temp_highest_accuracy = temp_node_evaluation;
                    temp_best_feature = feature_set;
                }
            }
        }

        cout << "Feature set {";
        for (int i = 0; i < temp_best_feature.size(); i++) {
            cout << temp_best_feature[i];
            if (i != temp_best_feature.size() - 1) {
                cout << ",";
            }
        }
        cout << "} was best, accuracy is " << temp_highest_accuracy << "%\n";

        if (temp_highest_accuracy >= highest_accuracy) {
            highest_accuracy = temp_highest_accuracy;
            best_feature = temp_best_feature;
            feature = temp_best_feature;
        } else {
            cout << "(Warning, Accuracy has decreased!)\n";
            break;
        }

        level++;
        if (level == featureNum) {
            done = true;
        }
    }

    cout << "Finished search!! The best feature subset is {";
    for (int i = 0; i < best_feature.size(); i++) {
        cout << best_feature[i];
        if (i != best_feature.size() - 1) {
            cout << ",";
        }
    }
    cout << "} which has an accuracy of " << highest_accuracy << "%\n";
}


int main()
{
    srand(time(NULL));
    cout << "Welcome to Group 11's Feature Selection Algorithm.\n";  
    int featureNum;
    int algNum;
    ifstream inputFile;
    int choice;
    cout << "input 1 to work on small dataset and 2 to work on large dataset" << endl;
    cin >> choice;
    if (choice == 1){
        featureNum = 10;
        inputFile.open("small-test-dataset.txt");
        if (inputFile.is_open()) {
        // File opened successfully
            cout<< "successfully imported small test dataset\n";
        } else {
            cout << "failed\n";
        }

        double array[100][11];
        double value;
        int colcount = 0;
        int rowcount = 0;
        while (inputFile >> value) {
            if(colcount == 10)
            {
                array[rowcount][colcount] = value;
                colcount =0;
                rowcount = rowcount + 1;
            }
            else{
                array[rowcount][colcount] = value;
                colcount++;  
            }
        }
        cout << "\nType the number of the algorithm you want to run.\n\n";
        cout << "      1) Forward Selection\n      2) Backward Elimination\n      3) Group 11's Special Algorithm.\n\n\n";
        cin >> algNum;
        if(algNum == 1)
        {
            greedyForward_s(featureNum, array);
        }
    } else if (choice == 2){
        featureNum = 40;
        ifstream inputFile2;
        inputFile2.open("large-test-dataset.txt");
        if (inputFile2.is_open()) {
        // File opened successfully
            cout<< "successfully imported large test dataset\n";
        } else {
            cout << "failed\n";
        }

        double array[1000][41];
        double value2;
        int colcount2 = 0;
        int rowcount2 = 0;
        while (inputFile2 >> value2) {
            if(colcount2 == 40)
            {
                array[rowcount2][colcount2] = value2;
                colcount2 =0;
                rowcount2 = rowcount2 + 1;
            }
            else{
                array[rowcount2][colcount2] = value2;
                colcount2++;  
            }
        }
    }else{
        cout << "invalid input, exit the program" << endl;
        exit(1);
    }
}

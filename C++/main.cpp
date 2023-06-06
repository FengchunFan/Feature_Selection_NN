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
/*
double greedyBackward(int featureNum)
{
    double bestOutcome = 0;
    double max = 0;
    double oldMax;
    int maxFeatureIndex = 0;
    int index;
    double accuracy;
    vector<int> num;
    vector<double> accuracys;
    vector<int> path;
    vector<double> allMax;
    int totalindex = 0;
    bool maxFlag = false;
    int totalRun = featureNum;
    if (featureNum == 0)
    {
        bestOutcome = eval();
        return bestOutcome;
    }
    for (int i = 0; i < featureNum; i++)
    {
        num.push_back(i + 1);
    }
    cout << "\nBeginning search.\n\n";
    for (int j = 0; j < totalRun; j++)
    {
        if (featureNum == 0)
        {
            break;
        }
        j = 0;
        index = 0;
        max = 0;
        maxFlag = false;
        for (int k = num.size() - 1; k >= 0; k--)
        {
            accuracy = eval();
            if (accuracy > max)
            {
                max = accuracy;
                index = k;
                if (max > oldMax)
                {
                    maxFlag = true;
                    maxFeatureIndex++;
                }
            }
            cout << "Using feature(s) {" << num[k] << "} accuracy is " << accuracy << "\n";
        }
        totalindex++;
        if (maxFlag == false)
        {
            cout << "(Warning, Accuracy has decreased!)\n";
        }
        path.push_back(num[index]);
        cout << "Feature set {";
        for (int m = 0; m < totalindex; m++)
        {
            if (m == totalindex - 1)
            {
                cout << path[m];
            }
            else
            {
                cout << path[m] << ",";
            }
        }
        cout << "} was best, accuracy is " << max << "\n";
        num.erase(num.begin() + index);
        num.erase(remove(num.begin(), num.end(), 0), num.end());
        featureNum--;
        oldMax = max;
        allMax.push_back(max);
    }

    for (int i = 0; i < allMax.size(); i++)
    {
        if (allMax[i] > bestOutcome)
        {
            bestOutcome = allMax[i];
            maxFeatureIndex = i + 1;
        }
    }

    cout << "FINISHED SEARCH!! The best feature subset is {";
    for (int m = 0; m < maxFeatureIndex; m++)
    {
        if (maxFeatureIndex == 0)
        {
            cout << path[m];
        }
        else
        {
            if (m == maxFeatureIndex - 1)
            {
                cout << path[m];
            }
            else
            {
                cout << path[m] << ",";
            }
        }
    }
    cout << "} which has an accuracy of " << bestOutcome << "\n";
    return bestOutcome;
}*/

void normal2(double (&arr)[][41], int row)
{
    double min = 44444;
    double max = -44444;
    //This portion here calculated the means of every feature so the columns excluding the first column
    for(int i = 1; i < 41;i++)
    {   
        for(int j = 0; j < row; j++)
        {
            if(arr[j][i-1] < min)
            {
                min = arr[j][i-1];
            }
            else if(arr[j][i-1]>max)
            {
                max = arr[j][i-1];
            }
        }
    }
    double denom = max-min;
    for(int i = 1; i < 41;i++)
    {   
        for(int j = 0; j < row; j++)
        {
            arr[j][i] = (arr[j][i] - min)/denom;
        }
    }
}
void normal(double (&arr)[][11], int row)
{
    double min = 44444;
    double max = -44444;
    //This portion here calculated the means of every feature so the columns excluding the first column
    for(int i = 1; i < 11;i++)
    {   
        for(int j = 0; j < row; j++)
        {
            if(arr[j][i-1] < min)
            {
                min = arr[j][i-1];
            }
            else if(arr[j][i-1]>max)
            {
                max = arr[j][i-1];
            }
        }
    }
    double denom = max-min;
    for(int i = 1; i < 11;i++)
    {   
        for(int j = 0; j < 100; j++)
        {
            arr[j][i] = (arr[j][i] - min)/denom;
        }
    }
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
        // Error opening the file
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
        normal(array, 100);
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
        normal2(array, 1000); //perform normalization
    }else{
        cout << "invalid input, exit the program" << endl;
        exit(1);
    }
    /*
    cout << "\nType the number of the algorithm you want to run.\n\n";
    cout << "      1) Forward Selection\n      2) Backward Elimination\n      3) Group 11's Special Algorithm.\n\n\n";
    cin >> algNum;
    if(algNum == 1)
    {
        if(choice == 1){
            greedyForward_s(featureNum, array);
        }else{
            //cout << "Using no features, I get an accuracy of " << greedyForward_l(0, array, choice) << endl;
            //greedyForward_l(featureNum, array, choice);
        }
    }
    else if(algNum == 2)
    {
       //cout << "Using no features and random evalution, I get an accuracy of " << greedyBackward(0);
       // greedyBackward(featureNum); 
    }

    
    //cout << "Using no features and random evalution, I get an accuracy of " << ;
    for(int i = 0; i < 100; i++)
    {
    for(int j = 0; j < 11; j++)
    {
        cout << array[i][j] << " ";
    }
    cout << endl;
    */
}
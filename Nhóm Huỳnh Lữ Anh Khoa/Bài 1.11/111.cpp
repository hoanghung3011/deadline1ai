#include<iostream>
#include<vector>
#include <windows.h>
using namespace std;
void inputTask(int& n, int& m, int arrBeginTime[100][100]) {
    cout << "Input n: ";
    cin >> n;
    cout << "\nInput m: ";
    cin >> m;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cout << "\n[" << i + 1 << "][" << j + 1 << "]: ";
            cin >> arrBeginTime[i][j];
        }
    }
}
void minTime(vector < int >& arrMachine, vector < int >& arrSumTime, int n, int m, int max, int arrBeginTime[100][100]) {
    for (int i = 0; i < m; i++) {
        int location = 0;
        int min = max;
        int machine = 0;
        for (int j = 0; j < n; j++) {
            if (min > arrBeginTime[i][j] && (arrMachine.at(j) == -1 || n < m)) {
                min = arrBeginTime[i][j];
                location = j;
                machine = i;
            }
        }
        arrMachine.at(location) = machine;
        arrSumTime.push_back(arrBeginTime[i][location]);
    }
}
void Assignment(vector < int >& arrMachine, vector < int >& arrSumTime, int n, int m, int max, int arrBeginTime[100][100]) {
    int h = m;
    while (h < n) {
        int minNguoi = max;
        int location = 0;
        for (int j = 0; j < m; j++) {
            if (minNguoi > arrSumTime.at(j)) {
                minNguoi = arrSumTime.at(j);
                location = j;
            }
        }
        int min = max;
        int loca = 0;
        for (int j = 0; j < n; j++) {
            if (min > arrBeginTime[location][j] && (arrMachine.at(j) == -1 || n < m)) {
                min = arrBeginTime[location][j];
                loca = j;
            }
        }
        arrMachine.at(loca) = location;
        arrSumTime.at(location) += min;
        h++;
    }
}
void WorkAssignment(vector < int >& arrMachine, vector < int >& arrSumTime, int n, int m, int arrBeginTime[100][100]) {
    for (int j = 0; j < n; j++) {
        arrMachine.push_back(-1);
    }
    int max = 2147483645;
    minTime(arrMachine, arrSumTime, n, m, max, arrBeginTime);
    Assignment(arrMachine, arrSumTime, n, m, max, arrBeginTime);
}
void outputTask(int n, vector < int > arrMachine) {
    cout << "\nWork assignment: ";
    for (int j = 0; j < n; j++) {
        cout << "\nWork " << j + 1 << " is assigned to machine No.";
        cout << arrMachine.at(j) + 1 << " ";
    }
}
int main() {
    int arrBeginTime[100][100];
    vector < int > arrSumTime;
    vector < int > arrMachine;
    int m, n;
    inputTask(n, m, arrBeginTime);
    WorkAssignment(arrMachine, arrSumTime, n, m, arrBeginTime);
    outputTask(n, arrMachine);
    system("pause");
    return 0;
}
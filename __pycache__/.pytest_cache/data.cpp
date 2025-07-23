#include <iostream>
using namespace std;

void inputValues(int values[], int size) {
    for (int i = 0; i < size; i++) {
        cout << "Enter value " << (i + 1) << " : ";
        cin >> values[i];
    }
}

int calculateTotal(int values[], int size) {
    int total = 0;
    for (int i = 0; i < size; i++) {
        total += values[i];
    }
    return total;
}

void showResult(int total) {
    cout << "==================" << endl;
    cout << "Result : " << total << endl;
}

int main() {
    const int SIZE = 5; 
    int values[SIZE];

    inputValues(values, SIZE);

    int total = calculateTotal(values, SIZE);

    showResult(total);

    return 0;
}
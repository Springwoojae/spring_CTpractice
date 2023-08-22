#include <iostream>
using namespace std;

int main(){
    double n;
    double max;
    double sum;
    double avg;

    cin >> n;
    max = sum = 0;

    for (int i = 1; i <= n; i++){
        double a;

        cin >> a;
        if (a > max)
            max = a;
        sum += a;
    }
    avg = (sum * 100) / (max * n);
    cout << avg << endl;
}
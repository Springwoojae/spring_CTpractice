#include<iostream>
using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {
        int sum = 0;
        double sum_avg = 0.0;
        int n;
        cin >> n;

        for (int j = 0; j < n; j++)
        {
            int c;
            double g;
            cin >> c >> g;
            sum += c;
            sum_avg += c * g;
        }
        double avg = sum_avg/sum;
        cout << fixed;
        cout.precision(1);
        cout << sum << " " << avg << endl;
    }
}
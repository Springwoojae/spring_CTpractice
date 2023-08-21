#include <iostream>
using namespace std;

int main(){
    int tc;
    cin >> tc;
    for (int i = 1; i <= tc; i++)
    {
        int d_1, d_2;
        
        cin >> d_1 >> d_2;
        cout << "Case " << i << ": " <<d_1 + d_2 << endl;
    }
    return 0;
}
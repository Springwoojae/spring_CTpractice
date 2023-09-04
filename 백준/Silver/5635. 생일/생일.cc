#include<iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    string name[n];
    int arr_y[n];
    int arr_m[n];
    int arr_d[n];
    int young;
    int old;
    // 어레이에 집어넣음
    for (int i = 0; i < n; i++)
    {
        string p;
        int d;
        int m;
        int y;

        cin >> p >> d >> m >> y;
        name[i] = p;
        arr_d[i] = d;
        arr_m[i] = m;
        arr_y[i] = y;
    }
    // 제일 어린놈
    int d = 1;
    int m = 1;
    int y = 1990;
    for (int i = 0; i < n; i++)
    {    
        if (y < arr_y[i])
        {
            y = arr_y[i];
            m = arr_m[i];
            d = arr_d[i];
            young = i;
        }
        else if (y == arr_y[i])
        {
            if (m < arr_m[i])
            {
                y = arr_y[i];
                m = arr_m[i];
                d = arr_d[i];
                young = i;
            }
            else if (m == arr_m[i])
            {
                if (d < arr_d[i])
                {
                    y = arr_y[i];
                    m = arr_m[i];
                    d = arr_d[i];
                    young = i;
                }                
            }
        }
    }
    // 제일 늙은놈
    int od = 31;
    int om = 12;
    int oy = 2010;
    for (int i = 0; i < n; i++)
    {    
        if (oy > arr_y[i])
        {
            oy = arr_y[i];
            om = arr_m[i];
            od = arr_d[i];
            old = i;
        }
        else if (oy == arr_y[i])
        {
            if (om > arr_m[i])
            {
                oy = arr_y[i];
                om = arr_m[i];
                od = arr_d[i];
                old = i;
            }
            else if (om == arr_m[i])
            {
                if (od > arr_d[i])
                {
                    oy = arr_y[i];
                    om = arr_m[i];
                    od = arr_d[i];
                    old = i;
                }                
            }
        }
    }
    cout << name[young] << '\n';
    cout << name[old];
}
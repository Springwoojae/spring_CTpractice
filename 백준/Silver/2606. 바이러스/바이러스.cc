#include<iostream>
#include<vector>

using namespace std;

vector<int>linked[101];
bool vst[101];
int cnt = 0;

void dfs(int s){
    vst[s] = true;
    for (int i = 0; i < linked[s].size(); i++)
    {
        int x = linked[s][i];
        if (!vst[x])
        {
            dfs(x);
            cnt++;
        }
    }
}


int main() {
    int com, link;

    cin >> com >> link;
    for (int i = 0; i < link; i++)
    {
        int r, c;
        cin >> r >> c;
        linked[r].push_back(c);
        linked[c].push_back(r);
    }

    dfs(1);

    cout << cnt << '\n';
}
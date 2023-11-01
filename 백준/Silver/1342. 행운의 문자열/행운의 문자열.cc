#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

string s;
int DAT[11];
vector<string>lst;

void lucky(string result){
    if(result.length() == s.length()){
        lst.push_back(result);
        return;
    }
    for (int i = 0; i < s.length(); i++){
        if(!DAT[i] && s[i] != result[result.length() - 1]){
            result.push_back(s[i]);
            DAT[i] = 1;
            lucky(result);
            result.pop_back();
            DAT[i] = 0;
        }
    }
}


int main(){
    string result;
    
    cin >> s;

    lucky(result);

    sort(lst.begin(), lst.end());
    lst.erase(unique(lst.begin(), lst.end()), lst.end());

    cout << lst.size() << '\n';
}
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;

vector<int> v;
bool isused[10];
int N, M;
//1~N까지 중복 없이 M개 고르기

void permutation(){
    if(v.size() == M){
        for(auto t : v){
            cout << t<< ' ';
        }
        cout<<'\n';
        return;
    }

    for(int i=1; i<=N; i++){
        if(!isused[i]){
        if(!v.empty() && v.back() > i ){
            continue;
        }
            isused[i] = true;
            v.push_back(i);
            permutation();
            v.pop_back();
            isused[i] = false;
        }
    }


}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    permutation();

}
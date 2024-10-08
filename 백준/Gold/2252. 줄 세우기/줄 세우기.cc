#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>
#include <deque>

using namespace std;
int N,M;
int ind[32001] = {0, };
int checks[32001] = {0, 1};

int main(){
    //11시16분 
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> adj[32001];
    cin >> N >> M;

    for(int i=0; i<M; i++){
        int a , b;
        cin >> a >> b;
        ind[b]++;
        checks[a] = 1;
        checks[b] = 1;
        adj[a].push_back(b);
    }

    queue<int> q;

    for(int i=1; i<N+1; i++){
        if(ind[i] == 0 ){
            q.push(i);
        }
    }

    queue<int> ans;

    while(!q.empty()){
        int cur = q.front();
        q.pop();
        cout << cur << ' ';

        for(auto it: adj[cur]){
            ind[it]--;
            if(ind[it] == 0){
                q.push(it);
            }
        }
    }

    for(int i=0; i<ans.size(); i++){
        //cout << ans.front() << ' ';
        ans.pop();
    }
    for(int i=1; i<N+1; i++){
        if(!checks[i]) cout << i << ' ';
    }


    
    

}
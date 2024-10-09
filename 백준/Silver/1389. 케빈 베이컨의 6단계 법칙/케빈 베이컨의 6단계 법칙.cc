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

vector<int> adj[101];

int bfs(int st, int en){
    int visited[101] = {0, };
    queue<int> q;
    q.push(st);
    visited[st] = 1;
    while(!q.empty()){
        int cur = q.front(); q.pop();
        if(en == cur) return visited[cur]-1;
        for(auto it: adj[cur]){
            //cout << it << ' ';
            if(!visited[it]) {
                q.push(it);
                visited[it] = visited[cur] + 1;
            }
        }
    }
    return 0;
}


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    
    int kevin[101] = {0, };

    //유저의 수, 친구 관계의 수
    int N, M;
    cin >> N >> M;
    for(int i=0; i<M; i++){
        int A, B;
        cin >> A >> B;
        adj[A].push_back(B);
        adj[B].push_back(A);
    }

    //bfs 여러 번하면 될 듯... 인접리스트?
    for(int i=1; i<N+1; i++){
        for(int j=1; j<N+1; j++){
            if (i==j) continue;
            //cout << i << ' ' << j << ' ' << bfs(i,j) << '\n';
            kevin[i] += bfs(i,j);
        }
    }

    int min_idx = 0;
    int min_val = 1e9;

    for(int i=1; i<N+1; i++){
        if(kevin[i] < min_val){
            min_val = kevin[i];
            min_idx = i;
        }
    }

    cout << min_idx;

}
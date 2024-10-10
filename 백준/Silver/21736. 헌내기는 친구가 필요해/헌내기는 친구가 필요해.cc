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

int N, M;
int campus[601][601];
int cr, cc;
int dr[] = {-1,1,0,0};
int dc[] = {0,0,-1,1};

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++){
            char c;
            cin >> c;
            campus[i][j] = c;
            if(c == 'I'){
                cr = i;
                cc = j;
            }
        }
    }

    queue<pair<int,int>> q;
    q.push({cr, cc});
    int visited[601][601] = {0, };
    int cnt = 0;

    while(!q.empty()){
        pair<int,int> p = q.front(); q.pop();
        cr = p.first;
        cc = p.second;
        if(campus[cr][cc] == 'P') cnt++;
        //cout << p.first <<' '<< p.second <<'\n';
        for(int i=0; i<4; i++){           
            int nr = cr + dr[i];
            int nc = cc + dc[i];
              
            //oob
            if(nr <0 || nc < 0 || nr > N-1 || nc > M-1) continue;
            else{
                if(!visited[nr][nc] && (campus[nr][nc] != 'X')){
                    //out << nr << ' ' << nc << '\n';  
                    q.push({nr,nc});
                    visited[nr][nc] = 1;
                }
            }
        }
    }

    if(cnt) cout << cnt;
    else cout << "TT";
    



}
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

int dr[] = {1,-1,0,0};
int dc[] = {0,0,-1,1};
char board[101][101] = {0, };
char normal[101][101] = {0, };
char abnor[101][101] = {0, };
int n;

void nor_bfs(int r, int c){
    queue<pair<int,int>> q;
    q.push({r,c});
    normal[r][c] = 1;
    while(!q.empty()){
        pair<int,int> cur = q.front(); q.pop();
        int cr = cur.first;
        int cc = cur.second;
        for(int i=0; i<4; i++){
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if(0<=nr && nr <n && 0<=nc && nc <n && !normal[nr][nc] && (board[nr][nc] == board[cr][cc])){
                {
                    q.push({nr,nc});
                    normal[nr][nc] = 1;
                }
            }
        }
    }
    
}

void abnor_bfs(int r, int c){
    queue<pair<int,int>> q;
    q.push({r,c});
    abnor[r][c] = 1;
    while(!q.empty()){
        pair<int,int> cur = q.front(); q.pop();
        int cr = cur.first;
        int cc = cur.second;
        for(int i=0; i<4; i++){
            int nr = cr + dr[i];
            int nc = cc + dc[i];
            if(0<=nr && nr<n && 0<=nc && nc <n && !abnor[nr][nc]){
                if((board[nr][nc] == board[cr][cc]) || (board[nr][nc] != 'B' && board[cr][cc] !='B'))
                {
                    q.push({nr,nc});
                    abnor[nr][nc] = 1;
                }
            }
        }
    }
    
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for(int i =0; i<n; i++){
        for(int j=0; j<n; j++){
            char c;
            cin >> c;
            board[i][j] = c;
        }
    }



    //bfs
    int nor_cnt = 0;
    int ab_cnt = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(normal[i][j] == 0){
                nor_bfs(i, j);
                nor_cnt++;
            }
            if(abnor[i][j] == 0){
                abnor_bfs(i, j);
                ab_cnt++;
            }
        }
    }

    cout << nor_cnt <<' '<< ab_cnt;

}
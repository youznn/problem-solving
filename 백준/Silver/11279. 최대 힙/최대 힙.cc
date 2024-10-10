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

int N;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    priority_queue<int> pq;
    for(int i=0; i<N; i++){
        int x;
        cin >> x;
        if(x == 0){
            if(pq.empty()) cout << 0 << '\n';
            else {cout << pq.top() << '\n'; pq.pop();}
        } else {
            pq.push(x);
        }
    }
}
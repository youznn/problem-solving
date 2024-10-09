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


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    priority_queue<int, vector<int>, greater<int>> pq;

    int N;
    cin >> N;
    for(int i=0; i<N; i++){
        int n;
        cin >> n;
        if(n == 0){
            if(pq.empty()) cout << 0 << '\n';
            else{
                cout << pq.top() << '\n'; pq.pop();
            }
        } else {
            pq.push(n);
        }
    }

}
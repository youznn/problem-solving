#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;

int card[500002];
int targets[500002];

int bs(int target, int st, int en){
    while(st <= en){
        int mid = (st+en)/2;
        if (card[mid] == target) return 1;
        else if(card[mid] < target){
            st = mid + 1;
        }
        else{
            en = mid - 1;
        }
    }
    return 0;

}

int main(){

    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N, M;
    cin >> N;
    for(int i=0; i<N; i++){
        cin >> card[i];
    }
    cin >> M;
    for(int i=0; i<M; i++){
        cin >> targets[i];
    }
    sort(card, card+N);

    //이분탐색
    for(int i=0; i<M; i++){
        cout << bs(targets[i], 0, N-1);
        if(i!=M-1) cout << ' ';
    }




}
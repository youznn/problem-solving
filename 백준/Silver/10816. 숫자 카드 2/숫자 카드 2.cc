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

int lower_bound(int target, int st, int en){
    int mid;
    while(st < en){
        mid = (st+en)/2;
        if(card[mid] >= target){
            en = mid;
        }
        else{
            st = mid + 1;
        }
        
    }
    return st;
    
}

int upper_bound(int target, int st, int en){
    int mid;
    while(st < en){
        mid = (st+en)/2;
        if(card[mid] > target){
            en = mid;
        }
        else{
            st = mid +1;
        }
        
    }
    return st;
    
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
        cout << upper_bound(targets[i], 0, N) - lower_bound(targets[i], 0, N) <<' ';
    }


}
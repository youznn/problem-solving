#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    int has[31] = {1, };
    
    for(int i=1; i<n+1; i++) has[i] = 1;
    
    for(auto it: reserve) has[it]++;
    for(auto it: lost) has[it]--;
    
    for(int i=1; i<n+1; i++) cout << has[i] << ' ';
    cout <<'\n';
    
    for(int i=1; i<n+1; i++){
        if(has[i]==0){
            if(i-1 > 0 && has[i-1] == 2){
                
                    has[i-1]--;
                    has[i]++;
                
            }
            else if(i+1 < n+1){
                if(has[i+1] == 2){
                    has[i+1]--;
                    has[i]++;
                }
            }
                
        }
    }
    
    for(int i=1; i<n+1; i++) cout << has[i] << ' ';
    
    for(int i=1; i<n+1; i++){
        if(has[i]) answer++;
    }
    return answer;
}
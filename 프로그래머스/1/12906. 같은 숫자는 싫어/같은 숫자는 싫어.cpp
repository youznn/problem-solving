#include <vector>
#include <iostream>
#include <stack>

using namespace std;

vector<int> solution(vector<int> arr) 
{   
    
    vector<int> v;
    for (auto it : arr){
        if(!v.empty()){
            if(v.back() == it) continue;
            v.push_back(it);
        } else {
            v.push_back(it);
        }
    }
    
    vector<int> answer = {v.begin(), v.end()};

    return answer;
}
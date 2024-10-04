#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    //앞에 있는 게 먼저 배포가 되어야지 뒤에 있는 것들도 배포가 됨
    //배포가 된 것들 stack에 쌓아 두기...
    
    //걸리는 날짜 저장
    queue<int> days;
    vector<int> answer;
    
    for(int i=0; i<progresses.size(); i++){
        int left = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
        days.push(left);
    }
    
    while(true){
        if(days.empty()) break;
        int cnt = 0;
        int cur = days.front();
        while(!days.empty() && days.front() <= cur ){
            days.pop();
            cnt++;
            cout << cnt << ' '; 
        } answer.push_back(cnt);
    }
    
    
    return answer;
}
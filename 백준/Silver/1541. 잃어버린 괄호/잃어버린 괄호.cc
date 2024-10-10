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
    // - 가 나오고, 앞에 - 가 있으면, 무조건 해당 마이너스부터 다시 묶기!
    // + 가 나오고, 앞에 - 가 있으면, -로 취급!! -면 다 마이너스다!
    // 앞이 +라면 그냥 그 연산자 따라가기
    // stack...!!!

    //식 정리하기
    string st;
    vector<int> nums;
    vector<char> ops;
    string cur = "";
    cin >> st;
    for(int i=0; i<st.size()+1; i++){
        char c = st[i];
        if((c != '+') && ( c != '-' )){
            //cout << c;
            cur += c;
        }
        else{
            ops.push_back(c);
            nums.push_back(stoi(cur));
            cur = "";
        }
    }

    nums.push_back(stoi(cur));
    if(!ops.empty()){

    int cur_ops = 1; //+ 0은 -
    int ans = nums[0];
    int idx = 0;
    for(int i=1; i<nums.size()+1; i++){
        if (cur_ops == 1){
            if(ops[idx++] == '+') cur_ops = 1;
            else cur_ops = 0;
            if (cur_ops == 1){
                ans += nums[i];
            } else {
                ans -= nums[i];
            }
        } else {
            ans -=nums[i];
            idx++;
        }
    }

    cout << ans;

    

    } else cout << st;

}
#include <string>
#include <vector>
#include <iostream>

using namespace std;

string recursion(vector<char>& s) {
    if (s.empty()) return "";

    vector<char> temp;
    int left = 0;
    int right = 0;

    for (auto it = s.begin(); it != s.end(); ++it) {
        if (*it == ')') {
            right++;
            if (!temp.empty() && temp.back() == '(') {
                temp.pop_back();
            } else {
                temp.push_back(')');
            }
        } else {
            left++;
            temp.push_back('(');
        }

        // 균형이 잡혔을 때 나누기
        if (right == left) {
            vector<char> next(it+1, s.end());
            string cur(s.begin(),it+1);
            //u는 균형잡힌 괄호 문자열
            if (temp.empty()) {
                //올바른 괄호 문자열이라면 문자열 v에 대해 다시 수행하기
                //u에 이어붙인 후 반환     
                cur += recursion(next);
                return cur;
            } else {
                //올바른 괄호 문자열이 아니라면
                string new_st = "";
                new_st += '(';
                new_st += recursion(next);
                new_st += ')';
                vector new_cur(cur.begin()+1, cur.end()-1);
                //나머지 문자열의 괄호 방향을 뒤집어?
                string rev_cur = "";
                for(auto i : new_cur){
                    if(i == '('){
                        rev_cur += ')';
                    } else {
                        rev_cur += '(';
                    }
                }
                
                string st = new_st + rev_cur;
                
                return st;

            }
        }
    }
}

string solution(string p) {
    if (p == "") return "";

    string temp_st = "";
    vector<char> s(p.begin(), p.end());
    string answer = recursion(s);

    return answer;
}

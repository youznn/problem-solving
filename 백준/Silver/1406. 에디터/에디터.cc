#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>

using namespace std;

int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  string s;
  list<char> L;
  int N;
  cin >> s;
  cin >> N;
  for(auto c : s) L.push_back(c);
  auto cursor = L.end();
  for(int i=0; i<N; i++){
    char op;
    cin >> op;
    if (op == 'P'){
      char temp;
      cin >> temp;
      L.insert(cursor, temp);
    }
    else if(op == 'L'){
      if(cursor != L.begin()) cursor--;
    }
    else if(op == 'D'){
      if(cursor != L.end()) cursor++;
    }
    else if(op == 'B'){
      if(cursor != L.begin()) {
        cursor--;
        cursor = L.erase(cursor);
      }

    }
  }
  for(auto t: L){
    cout << t;
  }
}
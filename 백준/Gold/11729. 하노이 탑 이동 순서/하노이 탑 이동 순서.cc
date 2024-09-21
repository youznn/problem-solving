#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <stack>
#include <queue>
#include <math.h>

using namespace std;
//boj 1914 재귀
//16:40 

int cnt;

void move(int N, int start, int end){
  cout << start << ' '<< end << '\n';
  return;
}

void hanoi(int n, int start, int via, int end){
  if(n == 1){
    move(n, start, end);
    return;
  }
  hanoi(n-1, start, end, via);
  move(n-1,start,end);
  hanoi(n-1,via, start, end);
  return;
}

int main(){
  ios::sync_with_stdio(0);
  cin.tie(0);
  unsigned long long int cnt;
  int N;
  cin >> N;
  cnt = pow(2,N) - 1;
  cout << cnt  << '\n';
  hanoi(N, 1, 2, 3);
}
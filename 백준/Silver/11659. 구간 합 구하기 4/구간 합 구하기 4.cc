//최대한 시간을 줄여야 할 듯
//일단 구간별로 앞에서부터 누적 합계를 구해서 vector에 저장.
//시작점까지의 합계를 뺌 

#include <iostream>
#include <string.h>
#include <vector>
#include <list>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;


int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n;
	int m;
	cin >> n >> m;
	int current;
	long long box[100002];
	box[0] = 0;
	for (int i = 1; i < n+1; i++) {
		cin >> current;
		box[i] = current + box[i - 1];
	}

	int a;
	int b;
	for (int i = 0; i < m; i++) {
		cin >> a;
		cin >> b;
		cout << box[b] - box[a-1] << "\n";
	}

}
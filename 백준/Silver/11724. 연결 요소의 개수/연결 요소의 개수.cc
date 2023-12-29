//최대한 시간을 줄여야 할 듯
//일단 구간별로 앞에서부터 누적 합계를 구해서 vector에 저장.
//시작점까지의 합계를 뺌 

#include <iostream>
#include <string.h>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>

using namespace std;

int main(void) {
	int n, m;
	cin >> n >> m;
	vector<int> nodes[1001];
	int start, end;
	set<int> notvisited;
	for (int i = 0; i < m; i++) {	
		cin >> start >> end;
		nodes[start].push_back(end);
		nodes[end].push_back(start);
		notvisited.insert(start);
		notvisited.insert(end);
	}
	int cnt = n-notvisited.size();

	while (notvisited.size()) {
		vector<int> stack;
		stack.push_back(*notvisited.begin());
		while (!stack.empty()) {
			int node = stack.back();
			stack.pop_back();
			if (notvisited.count(node)) {
				notvisited.erase(node);
				for (int v : nodes[node]) {
					if(notvisited.count(v)) stack.push_back(v);
				}
			}
		}
		cnt++;
	}
	cout << cnt;

}
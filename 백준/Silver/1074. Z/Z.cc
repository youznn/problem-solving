//라이브러리 최대한 쓰지 않고 구현해 보기

#include <iostream>
#include <math.h>


using namespace std;

int search(int n, int r, int c, int visited=0) {
	if (n == 1) {
		if (r == 1) {
			visited += 2;
		}
		if (c == 1) {
			visited += 1;
		}
		return visited;
	}
	else {
		int offset = pow(2, n * 2 - 2);
		int powerd2 = pow(2, n)/2;
		if (r >= powerd2) {
			r -= powerd2;
			visited += offset * 2;
		}

		if (c >= powerd2) {
			c -= powerd2;
			visited += offset;
		}
		return search(n - 1, r, c, visited);
	}
}


int main(void) {
	int n; 
	int r;
	int c;
	cin >> n >> r >> c;
	cout << search(n,r,c);
	return 0;
}
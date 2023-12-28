//일단 이건 dp다. 

#include <iostream>
#include <string.h>
#include <vector>
#include <list>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;

int main(void) {
	//implement vector
	vector<long long> spiral = { 1,1,1,2,2,3,4,5 };
	for (int i = 0; i < 93; i++) {
		spiral.push_back(spiral[7+i] + spiral[3+i]);
	}

	int t; //num of test cases
	cin >> t;
	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
		cout << spiral[n - 1] << endl;
	}
	
	return 0;
}
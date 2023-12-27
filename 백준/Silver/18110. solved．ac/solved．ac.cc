#include <iostream>
#include <string.h>
#include <vector>
#include <list>
#include <cmath>
#include <numeric>
#include <algorithm>

using namespace std;

int main(void) {
	int n;
	int cut;
	cin >> n;
	if (n == 0) {
		cout << 0;
		return 0;
	}

	vector<int> nums;

	for (int i = 0; i < n; i++) {		
		int num;
		cin >> num;
		nums.push_back(num);
	}

	sort(nums.begin(), nums.end());
	cut = round(n * 0.15);

	double sum = accumulate(nums.begin()+cut, nums.end()-cut, 0);

	double level = round(sum / (n - cut*2));
	cout << level;

	return 0;
}
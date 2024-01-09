#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main(int argc, char** argv)
{
	int n;
	cin >> n;

	for (int i = n-1; i > 0; i--) {
		for (int j = 0; j < n; j++) {
			if (j>=i) cout << "*";
			else cout << " ";
		}
		cout << "\n";
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (j >= i) cout << "*";
			else cout << " ";
		}
		if(i!=n-1) cout << "\n";
	}

	return 0;
}
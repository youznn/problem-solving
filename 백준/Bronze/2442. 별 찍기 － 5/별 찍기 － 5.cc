#include <iostream>
#include <math.h>


using namespace std;


int main(void) {
	int n; 
	cin >> n;
	int row = n * 2 - 1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < row; j++) {
			if (j < (row/2-i)){
				cout << " ";
			}
			else if (j > (row/2+i)) {
			}
			else {
				cout << "*";
			}
		}
		if(i<n-1)cout << "\n";
	}
}
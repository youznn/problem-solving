
#include <iostream>
#include <math.h>


using namespace std;


int main(void) {
	int n; 
	cin >> n;
	for (int i = n; i > 0; i--) {
		for (int j = 0; j < i; j++) { cout << "*"; }
		cout << "\n";
	}
}
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;
int N;

int main(){
	cin >> N;
	for(int i=0; i<N; i++){
		for(int j=0; j<N-i-1; j++){
			cout <<" ";
		}
		for(int j=N-i-1; j<N+i; j++){
			if(N % 2 == 1){
			if ((i + j) % 2 == 1){
				cout <<" ";
			}
			else{
				cout << "*";
			}
			}
			else{
				if ((i + j) % 2== 0){
				cout <<" ";
			}
			else{
				cout << "*";
			}
			}
			
		}
		cout << endl;
	}
}
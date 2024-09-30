#include <string>
#include <vector>
#include <iostream>

using namespace std;

int pick[1000] = {0, }; //0은 안 뽑음, 1은 뽑음, 2는 패스함
int step = 1;
int life = 0;
//카드를 내면 다음 라운드로 이동 가능함. 

int solution(int coin, vector<int> cards) {
    //초반 n/3개 뽑기
    int n = cards.size();
    for(int i=0; i<n/3; i++){
        pick[cards[i]] = 1;
    }
    //초반 카드 중에서 쌍 찾기
    for(int i=0; i<n/3; i++){
        if(pick[n+1-cards[i]]){
            life++;
        }
    }
    //쌍 다 찾았으면 나누기 2 해줘야 함
    life /= 2;
    
    //두개씩 뽑기 시작
    int first_idx = n/3;
    int second_idx = first_idx + 1;
    
    while (second_idx < n && life >= 0) {
        //카드 뽑기.
        //인덱스 옮겨주기
        int fir_c = cards[first_idx];
        int sec_c = cards[second_idx];
        
        first_idx += 2;
        second_idx += 2;
        
        //코인 있어야 가능
        if(coin){    
        //내가 가진 카드 리스트에 나머지 부분이 있는지 확인
        if(pick[n+1-fir_c] == 1){
            //있으면 뽑아
            pick[fir_c] = 1;
            cout << "pick " << fir_c << '\n';
            coin--;
            life++;
        } else {
            pick[fir_c] = 2;
        }
        }
        if (coin) {
        if(pick[n+1-sec_c] == 1){
            //있으면 뽑아
            pick[sec_c] = 1;
            coin--;
            life++;
        } else {
            pick[sec_c] = 2;
        }
        }
        //다음으로 life를 제공해야 함
        //life가 0일 경우에는 다시... 생각을...
        
        if(life == 0){
            if(coin >= 2){
            for(int i=0; i<n+1; i++){
                if(pick[i] == 2 && pick[n+1-i] == 2){
                    pick[i] = 1; pick[n+1-i] = 1;
            
                    life++;
                    coin -=2;
                    break;
                }
                } 
            }
            else break;
        }
        

        if(life == 0) break;
        
    
        life--;
        step++;
    
        
    }
    
    
    
    
    
    int answer = step;
    return answer;
}
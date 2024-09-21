#include <string>
#include <vector>
#include <iostream>

using namespace std;
//21:00

vector<int> solution(vector<vector<int>> edges) {
    
    int in_nodes[1000002] = {0};
    int out_nodes[1000002] = {0};
    
    //시작정점은 in이 0개, out이 2개 이상
    //막대의 개수는 out이 0인 노드의 개수와 같음
    //8자의 개수는 in이 2이상, out이 2인 노드의 개수와 같음
    //도넛의 개수는 정점의 out개수 - (막대+8자) 의 개수와 같음
    int max_num;
    for(auto it : edges){
        in_nodes[it[1]] += 1;
        out_nodes[it[0]] += 1;
    }
    
    
    int start_node;
    int donut = 0;
    int eight = 0;
    int stick = 0;
    
    for(int i=1; i<1000001; i++){
        if(in_nodes[i] == 0 && out_nodes[i] == 0) continue;
        if(in_nodes[i] == 0 && out_nodes[i] >= 2) start_node = i;
        else if(out_nodes[i] == 0) stick++;
        else if(in_nodes[i] >= 2 && out_nodes[i] == 2) eight++;
    }
    
    donut = out_nodes[start_node] - (stick + eight);
    
    vector<int> answer = {start_node, donut, stick, eight};
    return answer;
}
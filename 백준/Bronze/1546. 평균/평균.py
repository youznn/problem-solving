from sys import stdin

n = int(input())
score_list = list(map(int,input().split()))
max_score = max(score_list)
new_score_list = [i/max_score*100 for i in score_list]
print(sum(new_score_list)/len(new_score_list))
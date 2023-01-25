from sys import stdin
word = input()

alpha_list = [-1 for i in range(26)]

for i in range (len(alpha_list)):
    for j in range(len(word)):
        if word[j] == chr(i+97):
            alpha_list[i] = j
            break

print(" ".join(map(str,alpha_list)))

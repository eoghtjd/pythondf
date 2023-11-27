import sys

input = sys.stdin.readline 

N, M = map(int, input().split())


S = set()
for i in range(N):
    string = input()
    S.add(string)

count = 0


for i in range(M):
    string_to_check = input()
    if string_to_check in S:
        count += 1

print(count)

from collections import deque
import sys
N, K = map(int,sys.stdin.readline().split(" "))
list1 = {}
for i in range(K) :
    n = str(sys.stdin.readline().strip())
    list1[n] = i
list1 = deque(map(lambda x : list(x),sorted(list1.items(),key = lambda x : x[1])))
for j in range(N):
    if list1 :
        print(deque.popleft(list1)[0])

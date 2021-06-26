from itertools import product
import sys
N, nk = list(map(int,sys.stdin.readline().strip().split(" ")))
K = sys.stdin.readline().strip().split(" ")

L = len(str(N))

while True :
    ans = ""
    N_list = sorted(list(map(lambda x : "".join(list(x)),product(K,repeat=L))),key = lambda x : int(x))
    while N_list :
        n = N_list.pop()
        if int(n) <= N :
            ans = n
            break;
    if ans == "":
        L -=1
    else :
        break;
print(ans)

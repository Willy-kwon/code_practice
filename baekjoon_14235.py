import heapq as h
import sys

N = int(sys.stdin.readline())

queue = []
h.heapify(queue)

for i in range(N) :
    cur = list(map(int,sys.stdin.readline().strip().split(" ")))
    if cur[0] == 0 :
        if queue :
            print(h.heappop(queue)[1])
        else :
            print(-1)
    else :
        for a in cur[1:] :
            h.heappush(queue,(-a,a))

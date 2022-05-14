import heapq as h
import sys

N = int(sys.stdin.readline().strip())

queue = []
h.heapify(queue)

for i in range(N) :
    cur = int(sys.stdin.readline().strip())

    if cur > 0 :
        h.heappush(queue,cur)
    else :
        if queue :
            print(h.heappop(queue))
        else :
            print(0)


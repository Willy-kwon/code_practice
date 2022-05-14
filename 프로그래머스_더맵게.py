import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        A = heapq.heappop(scoville) 
        if A >= K:
            break;
        elif len(scoville) == 0 :
            answer = -1
            break;
        else :
            B = heapq.heappop(scoville)
            result = A+2*B
            heapq.heappush(scoville,result)
            answer +=1
        
    return answer

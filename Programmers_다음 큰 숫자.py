from collections import Counter
def to2(n):
    ans=""
    while n > 0 :
        l = n%2
        ans = str(l) +ans
        n = n//2
    return ans
def solution(n):
    n1 = Counter(to2(n))["1"]
    while True :
        answer = n + 1
        next_n1 = Counter(to2(answer))["1"]
        if n1 == next_n1 :
            break;
        else :
            n =n+1
    return answer
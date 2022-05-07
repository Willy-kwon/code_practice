def solution(prices):
    answer =[0 for i in prices]
    for i in range(len(prices)) :
        P1 = prices[i]
        stack = [P1]
        for j in range(i+1,len(prices)) :
            P2 = prices[j]
            if P1 <= P2 :
                stack.append(P2)
            else :
                stack.append(P2)
                break;
        answer[i] = len(stack)-1
    return answer

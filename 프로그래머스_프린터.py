from collections import deque
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    idx_list = deque([p for p in range(len(priorities))]);
    
    
    while priorities :
        cur = deque.popleft(priorities);
        idx = deque.popleft(idx_list);
        if priorities :
            max1 = max(priorities)
            if max1 > cur :
                priorities.append(cur);
                idx_list.append(idx);
            else :
                answer +=1
                if idx == location :
                    break;
        else :
            answer +=1
    return answer

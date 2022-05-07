from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = truck_weights[::-1];
    cur = deque([]);
    weights_list = deque([]);
    cur_weight = 0;
    
    temp = []
    while truck_weights :
        if cur and cur[0] == 0 :
            w = deque.popleft(weights_list)
            deque.popleft(cur)
            cur_weight -= w
            temp.append(w)
        truck = truck_weights.pop()
        if cur_weight + truck <= weight :
            cur_weight += truck;
            cur.append(bridge_length);
            weights_list.append(truck);
            cur = deque([c-1 for c in cur]);
            answer +=1;
        else :

            if cur :
                truck_weights.append(truck)
                t = cur[0];
                cur = deque([c-t for c in cur]);
                answer += t
    if cur :
        answer += (cur.pop()+1)
    return answer
  
  def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    current_queue = deque()
    current_count = deque()
    count = 0
    while truck_weights:
        current_count = deque(map(lambda x : x+1,current_count))
        if bridge_length in current_count :
            deque.popleft(current_queue)
            deque.popleft(current_count)
        if sum(current_queue) +truck_weights[0] <= weight:
            s1 = deque.popleft(truck_weights)
            deque.append(current_queue,s1)
            deque.append(current_count,0)
        count+=1
    if current_count :
        count = count +  (bridge_length- current_count.pop())
    answer = count
    return answer

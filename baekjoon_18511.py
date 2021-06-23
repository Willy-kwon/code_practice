from collections import Counter
import sys
N = sys.stdin.readline().strip()

Word_list = list(map(list,Counter(N).items()))

odds = [w for w in Word_list if w[1] %2 == 1]
evens =[w for w in Word_list if w[1] %2 == 0]
if odds and odds[0][1] > 1:
    odds[0][1] -= 1
    evens.append(odds[0])
evens = sorted(evens)
if len(odds) > 1 :
    print("I'm Sorry Hansoo")
else :
    W = "".join(list(map(lambda x: x[0] * (x[1] // 2), evens)))
    if odds :
        print(W+odds[0][0]+W[::-1])
    else :
        print(W+W[::-1])

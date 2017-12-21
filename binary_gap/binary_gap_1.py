# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from random import randint

def solution(N):
    # write your code in Python 3.6
    C, TC = None, 0
    while N > 0:
        R = N % 2
        N = N //2
        if (R == 1):
            if C is not None and C > TC:
                TC  = C
            C = 0
        else:
            if C is not None:
                C += 1

    return TC

print(solution(1041), bin(1041))
print(solution(256), bin(256))
print(solution(6), bin(6))
print(solution(328), bin(328))


for i in range(100):
    S = randint(1,2147483647)
    print(solution(S), bin(S))
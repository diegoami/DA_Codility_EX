# you can write to stdout for debugging purposes, e.g.

def solution(X, A):
    L = [0]*X
    ES = X*(X+1)/2
    S = 0
    for i,e in enumerate(A):
        if L[e-1] == 0:
            S += e
            L[e-1] = 1
            if (S == ES):
                return i
    return -1

print(solution (5,[1, 3, 1, 4, 2, 3, 5, 4]))
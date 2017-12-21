
def solution(N, A):
    L = [0]*N
    m = 0
    lm = 0
    for x in A:
        if x <= N:
            if (L[x-1]) < lm:
                L[x-1] = lm
            L[x-1] += 1
            if (L[x-1]) > m:
                m = L[x-1]
        else:
            lm = m


    return [max(x,lm) for x in L]

print(solution (5, [3, 4, 4, 6, 1, 4, 4]))
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if (len(A)) < 2:
        return 0
    else:
        MC = 0
        MS = 0
        for i,x in enumerate(A):
            DV = (x - A[i-1]) if i > 0 else 0
            MC = max(MC+DV,0)
            MS = max(MS, MC)

        return MS


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))
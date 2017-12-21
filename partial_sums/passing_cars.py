
def solution(A):
    S = sum(A)
    TS = 0
    PC = 0
    for x in A:
        if x == 0:
            PC += S - TS
        else:
            TS += 1
        if PC > 1000000000:
            return -1
    return PC


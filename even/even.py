# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    V = set()
    for x in A:
        if x in V:
            V.remove(x)
        else:
            V.add(x)

    return V.pop()

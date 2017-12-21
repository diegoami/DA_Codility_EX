# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    V = set()
    for elem in A:
        V.add(elem)
    c = 1
    while c in V:
        c += 1
    return c

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    ES = N*(N+1)/2
    S = sum(A)
    return ES-S
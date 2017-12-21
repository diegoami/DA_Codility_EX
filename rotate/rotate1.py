# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    B = list(A)
    N = len(A)
    for i, e in enumerate(A):
        B[(i+K)%N]=e

    return B

print(solution([3, 8, 9, 7, 6] ,3))
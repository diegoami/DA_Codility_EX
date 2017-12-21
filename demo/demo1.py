# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solutionB(A):
    # write your code in Python 3.6
    N = len(A)

    V = dict()
    for i, elem in enumerate(A):
        V[elem] = V.get(elem,0)+1
    c = 1
    while c in V:
        c += 1
    return c

print(solutionB([1, 3, 6, 4, 1, 2]))
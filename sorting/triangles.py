class TriangleException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

def solution(A):
    found = False

    def search_in_A(A):
        N = len(A)
        if N == 1 or N == 0:
            return A
        else:
            pN = N //2
            lA = A[:pN]
            uA = A[pN:]
            lsA = search_in_A(lA)
            usA = search_in_A(uA)
            cl, cu = 0,0
            rL = []
            rindex = 0
            while cl < len(lsA) or cu < len(usA):
                if (cu >= len(usA)):
                    rL.append(lsA[cl])
                    cl += 1
                elif (cl >= len(lsA)):
                    rL.append(usA[cu])
                    cu += 1
                else:
                    if lsA[cl] <= usA[cu]:
                        rL.append(lsA[cl])
                        cl += 1
                    else:
                        rL.append(usA[cu])
                        cu += 1
                rindex += 1
                if (rindex >= 3):
                    p,q,r = rL[-3],rL[-2],rL[-1]
                    if p+q > r and p+r>q and q+r>p:
                        raise TriangleException("Triangle Found")

        return rL

    try:
        search_in_A(A)
        return 0
    except TriangleException:
        return 1

print(solution([16,25]))
print(solution([10,2,5,1,8,20]))
print(solution([3,16,25]))
def getGreedySum(L, s):
    M = []
    for l in L:
        if l > s:
            M.append(0)
        else:
            m = int(s/l)
            s = s - m*l
            M.append(m)
    return M

def applyM(M,L):
    s = 0
    for idx in range(len(M)):
        s += M[idx] * L[idx]
    return s

def greedySum(L, s):
    M = getGreedySum(L, s)
    s1 = applyM(M, L)
    if s1 != s:
        return 'no solution'
    else:
        return sum(M)

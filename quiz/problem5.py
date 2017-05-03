def mk_subseq(L):
    if L:
        lsts = []
        for idx in range(len(L) + 1):
            lsts.append(L[:idx])
        res = lsts + mk_subseq(L[1:])
    else:
        res = []
    return res

def max_sum_subseq(L):
    max_sum=-1e10
    for l in L:
        s = sum(l)
        if s > max_sum: max_sum = s
    return max_sum

def max_config_sum(L):
    return max_sum_subseq(mk_subseq(L))

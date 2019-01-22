from functools import lru_cache

denominations = [1, 4, 7, 13, 28, 52, 91, 365]


def candidates(n):
    return [bill for bill in denominations if bill <= n]


def bills_greedy(n):
    if n == 0:
        return []
    cands = candidates(n)
    if cands == []:
        raise RuntimeError("no solution found")
    largest_candidate = max(cands)
    s = bills_greedy(n - largest_candidate)
    return s + [largest_candidate]


def bills_dyn_prog(n):
    if n == 0:
        return []
    cands = candidates(n)
    if cands == []:
        raise RuntimeError("no solution found")
    solutions = [bills_greedy(n - cand) + [cand] for cand in cands]
    return min(solutions, key=len)

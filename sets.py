from __future__ import print_function


def difference(S, T):
    return [e for e in S if e not in T]


def union(S, T):
    return difference(S, T) + T


def intersection(S, T):
    return [e for e in union(S, T) if e in S and e in T]


def symmetric_difference(S, T):
    return difference(S, T) + difference(T, S)


def cartesian_product(S, T):
    return [(e1, e2) for e1 in S for e2 in T]


def test():
    print(intersection([1, 2, 3], [2, 3, 4]))


if __name__ == '__main__':
    test()

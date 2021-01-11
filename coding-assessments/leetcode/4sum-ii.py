from collections import Counter
def fourSumCount(A:[int], B:[int], C:[int], D:[int]) -> int:
    ab = Counter([a+b for a in A for b in B])
    cd = [c+d for c in C for d in D]
    count = 0
    for num in cd:
        count += ab[-num]
    return count;



fourSumCount(
A = [ 1, 2],
B = [-2,-1],
C = [-1, 2],
D = [ 0, 2]
)
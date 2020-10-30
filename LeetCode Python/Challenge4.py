def numSubarraysWithSum(A, S):
    """
    :type A: List[int]
    :type S: int
    :rtype: int
    """
    P = [0]
    for i in A:
        P.append(P[-1] + i)
    return P
            
    ans = 0

print(numSubarraysWithSum([1,0,1,0,1], 2))
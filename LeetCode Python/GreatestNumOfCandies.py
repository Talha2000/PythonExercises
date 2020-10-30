def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """

    maxCandies = max(candies)
    for i in range(len(candies)):
        if ((candies[i] + extraCandies) == maxCandies):
            candies[i] = True
        elif ((candies[i] + extraCandies) >= maxCandies):
            candies[i] = True
        else:
            candies[i] = False
    return candies


print(kidsWithCandies([2,3,5,1,3], 3))


        
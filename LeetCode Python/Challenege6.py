def longestPrefix(s):
    """
    :type s: str
    :rtype: str
    """
    for i in range(len(s)-1, 0, -1):
        P = s[0:i]
        S = s[len(s)-i: len(s)]

        if P == S:
            return s[0:i]
    return ""
        
print(longestPrefix("ababab"))     
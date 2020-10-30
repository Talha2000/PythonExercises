def reverseOnlyLetters(S):
    """
    :type S: str
    :rtype: str
    """
    lst = []
    for i in S: # Go through all the letters in the string and append to the list if alphabet
        if i.isalpha():
            lst.append(i)        
    ans = []
    for j in S:
        if not j.isalpha():
            ans.append(j)
        else:
            ans.append(lst.pop()) #replaces the letters in lst with the last letters in S
    return "".join(ans)

print(reverseOnlyLetters("a-bC-dEf-ghIj"))
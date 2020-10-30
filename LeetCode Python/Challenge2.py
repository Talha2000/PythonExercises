
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    open_para = ['(', '[', '{']
    stack = []
    s = list(s)
    for i in s:
        if i in open_para:
            stack.append(i)
        else:
            if stack == []:
                return False

            c = stack.pop()
            if c == '(' and i != ')':
                return False
            if c == '{' and i != '}':
                return False
            if c == '[' and i != ']':
                return False
    
    if stack != []:
        return False
    return True
        
        
        


print(isValid("()[]{}"))
        
        
        
        
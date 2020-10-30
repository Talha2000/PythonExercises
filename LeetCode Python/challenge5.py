def letterCombinations(digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        
        
        def track(combination, digits):
            if len(digits) == 0:
                result.append(combination)
            else:
                for i in phone[digits[0]]:
                    track(combination + i, digits[1:])
             
            
        result = []
        if digits:
            track("", digits)
        return result

print(letterCombinations('23'))
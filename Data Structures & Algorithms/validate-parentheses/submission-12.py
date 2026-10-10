class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketMap = {')': '(', ']': '[', '}': '{'}

        '''
            strings only have the bracket characters
            ok so how do you normally check?
            you start by reading the string
            push every open bracket onto the stack
            when you land on a closed bracket, compare to see if its value matches tos
            if no, false
            if yes, pop tos
            keep going until tos -1
        '''

        stack = []
        top = -1

        for c in s:
            if c in bracketMap:
                if stack and stack[-1] == bracketMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
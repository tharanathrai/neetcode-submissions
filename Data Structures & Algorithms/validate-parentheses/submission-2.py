class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # matched and resolved parentheses
                    stack.pop()
                else:
                    return False # fake news
            else:
                stack.append(c)

        return True if not stack else False
import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opSet = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda v1, v2: int(v1 / v2)
        }

        for t in tokens:
            if stack and t in opSet:
                v2 = stack.pop()
                v1 = stack.pop()
                comp = opSet[t](v1, v2)
                stack.append(comp)
            else:
                stack.append(int(t))
        return stack.pop()
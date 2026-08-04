# Last updated: 04/08/2026 11:37:35
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack= []
        ops = {
            "+": lambda a, b: int(a + b),
            "-": lambda a, b: int(a - b),
            "*": lambda a, b: int(a * b),
            "/": lambda a, b: int(float(a) / b)
        }

        for t in tokens:
            if t in ops:
                temp = ops[t](stack[-2], stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)         
            else:
                stack.append(int(t))
        return stack[0]
                
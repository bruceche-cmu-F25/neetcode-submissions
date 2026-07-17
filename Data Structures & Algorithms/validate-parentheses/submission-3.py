from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # stack = deque()

        # for char in s:
        #     stack.append(char)

        # for i in range(len(s)//2):
        #     if s[i] == '(':
        #         if not stack.pop() == ')':
        #             return False
        #     elif s[i] == '[':
        #         if not stack.pop() == ']':
        #             return False
        #     elif s[i] == '{':
        #         if not stack.pop() == '}':
        #             return False
        # return True
        # stack = deque()

        # for char in s:
        #     if char == '(' or char == '[' or char == '{':
        #         stack.append(char)

        #     elif char == ')':
        #         if not stack or stack.pop() != '(':
        #             return False

        #     elif char == ']':
        #         if not stack or stack.pop() != '[':
        #             return False

        #     elif char == '}':
        #         if not stack or stack.pop() != '{':
        #             return False

        # return len(stack) == 0
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return not stack

        


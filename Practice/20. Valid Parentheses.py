'''
Task Details
    Platform: LeetCode
    Name: 20. Valid Parentheses
    Link: https://leetcode.com/problems/valid-parentheses
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ('(', '[', '{')
        for i in s:
            if i in opening:
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                _pop = stack.pop()
                if (i == ']' and _pop == '[') or (i == '}' and _pop == '{') or (i == ')' and _pop == '('):
                    pass
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False
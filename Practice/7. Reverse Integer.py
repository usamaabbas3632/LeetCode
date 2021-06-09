'''
Task Details
    Platform: LeetCode
    Name: 7. Reverse Integer
    Link: https://leetcode.com/problems/reverse-integer/
'''

class Solution:
    def reverse(self, x: int) -> int:
        neg = None
        if x<0:
            x*=-1
            neg = 1
        x = int(str(x)[::-1])
        if neg:
            x = -x
        
        if -2**31 <= x <= 2**31 -1:
            return x
        else:
            return 0
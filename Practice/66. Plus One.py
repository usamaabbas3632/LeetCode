'''
Task Details
    Platform: LeetCode
    Name: 66. Plus One
    Link: https://leetcode.com/problems/plus-one/
'''

class Solution:
    def plusOne(self, digits):
        index = len(digits) - 1
        adding_one = False
        while index >= 0:
            digits[index] += 1
            if digits[index] != 10:
                adding_one = False
                break
            else:
                adding_one = True
                digits[index] = 0
                index -= 1
        if adding_one:
            digits.insert(0, 1)
        return digits

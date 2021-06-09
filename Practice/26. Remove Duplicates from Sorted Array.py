'''
Task Details
    Platform: LeetCode
    Name: 26. Remove Duplicates from Sorted Array
    Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        prev_elem = None
        _len = 0
        while i < len(nums):
            if nums[i] == prev_elem:
                i += 1
            else:
                prev_elem = nums [j] = nums[i]
                _len += 1
                i += 1
                j += 1
        return _len

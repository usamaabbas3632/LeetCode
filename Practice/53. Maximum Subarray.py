'''
Task Details
    Platform: LeetCode
    Name: 53. Maximum Subarray 
    Link: https://leetcode.com/problems/maximum-subarray/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        '''
        #Simple Brute Force Algorithm
        
        max_sum = nums[0]
        for i in range(1, len(nums)+1):
            for j in range(0, len(nums)):
                if sums[i][i] not None
                
                _sum = sum(nums[j:j+i])
                #print(f'{i=}, {j=}, {_sum=}')
                if _sum > max_sum:
                    max_sum = _sum
        return max_sum
        '''
        
        # Kadane's Algo
        # https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
        
        local_max = 0
        global_max = -1000000
        
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i]+local_max)
            if local_max > global_max:
                global_max = local_max
        return global_max

# Given a binary array nums, return the maximum number of consecutive 1's in the array

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        solution = 0
        
        for item in nums:
            if item == 1:
                count += 1
            else: 
                if count > solution:
                    solution = count 
                count = 0
            if count > solution:    # Added here because if the array ends before the longest streak ends then it wasn't working properly
                solution = count
                
        return(solution)
# Given an array of integers, return how many of them contain an even number of digits
# I'm assuming this is simple enough and I can just do a for loop, using an if statement to increase the count if the length of the int is odd (because length starts at 0?)


class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        
        for item in nums:
            if len(str(item)) % 2 == 0:     # Need to convert the int into a string, then get the length of that first, or it throws an error
                count += 1
        return(count)
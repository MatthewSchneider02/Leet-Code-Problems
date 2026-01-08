#Given integer array nums and integer val
#Loop over nums and remove everywhere val appears
#Return the amount of int in nums that are not equal to val
    #May not have to remove val from nums, just count how many times val appears, then subtract from length(nums) and return that count
    #Ha actually just kidding the instructions are dumb. They need the list of nums with the val taken out. Why is this question phrased dumb?

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


        
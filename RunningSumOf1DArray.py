class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        i = 0
        array = []

        for num in nums:
            if i == 0:
                array.append(nums[i])
            else:
                array.append(nums[i] + array[i-1])
            i += 1

        return array
# Given an int array, sort it in non decreasing order (like increasing, but can contain duplicates), then return an array of the squares of each number, also sorted in non-decreasing order

# So if there are no negative numbers, we can just square the number in the array and return it back because it will already be in non decreasing order
# But the example array has negatives, so we should expect that

# I think I should first square each number in the array and append to a new array
# Then I think python has a built in sort function for lists


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredNums = []
        
        for item in nums:
            squaredNums.append(item * item)
        
        squaredNums.sort()  # Have to sort on a separate line from return, can't combine them into one line
        return(squaredNums)
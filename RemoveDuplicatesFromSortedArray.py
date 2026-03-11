# Integer array nums is sorted in non-decreasing order (this means increasing order but can include duplicates)
# Remove the duplicates while keeping the relative order of the elements
# Return the number of unique numbers, then array nums sorted in increasing order instead of non-decreasing order

# So we want to iterate through the nums array, keeping track of what the last number was
    # If the number we are currently looking at is the same as the previous, pop that off the array
    # If it's not, move onto the next number and repeat until through the entire array
# Best way to count the unique elements in num? Count as we iterate through the array or is it as simple as .len() at the end of the iterations?

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 1

        while i < len(nums):            #Switched from a for loop to a while loop because when using pop it would cause indexing issues with the array 
            previous_num = nums[i-1]
            if nums[i] == previous_num: 
                nums.pop(i)
            else: 
                i += 1

    
        return (len(nums))
    

# Also, despite what the leetcode examples give, they don't need the length/amount of unique numbers? Just the sorted array ig
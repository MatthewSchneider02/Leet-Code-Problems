# Given two int arrays, nums1 and nums2. They are sorted in non-decreasing order.
# You are also given two ints m and n, giving the number os elements in each array
# Merge them into a single array sorted in non-decreasing order 
# The returned array should be nums1, not a new array

# So this problem, assuming I was using javascript, declared nums1 array with a length of m + n, with the last n elements set to 0
    # We need to remove these for python
# Then, we can just append the elements in nums2 to the end of nums1 (while loop with i count for the element?)
# Then we can sort nums1 with the sort function
# Return nums1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        i = 0
        
        while i < len(nums2):
            nums1.append(nums2[i])
            i += 1
            
        nums1.sort()
        return(nums1)
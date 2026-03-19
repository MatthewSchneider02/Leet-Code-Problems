# Given a fixed-length int array, duplicate each occurrence of 0, shifting the remaining elements to the right

# Should use a while loop because we are going to be changing the array as we loop through it
# if item is 0, push 0 at that location

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        start_array_length = len(arr)
        
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2  # Having i increase by 2 here stops the loop from running infinitely and cloning all the 0's forever
            else:
                i += 1
        
        del arr[start_array_length:]    # Added this here because the question says they don't care about anything past the original array length.
        return(arr)
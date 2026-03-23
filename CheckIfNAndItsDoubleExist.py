# Given int array arr
# Check if there exists two indices (i and j) such that
    # i != j
    # 0 <= i
    # j < arr.length
    # arr[i] == 2 * arr[j]

# Should we sort the array first, then do binary searching?
# Sort the array with the built in python function
# Check value at index length/2
    # Set num1 = value
        # Check value at index 3 * (length/4)
            # If value is 2 * num1 return true
            # If value is > 2 * num1 then check the value at
    # if value is  == 0, check value at index 3 * (length/4)
# Actually I feel like this is too annoying to deal with, a nested for loop in a for loop checking each value after sorting sounds easier mentally

# Actually sorting doesn't matter here because I misread the problem. The indice i cannot be negative, but the solution values can be
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
            
        for num in arr:
            if 2 * num in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
                
                
        return False
            
        
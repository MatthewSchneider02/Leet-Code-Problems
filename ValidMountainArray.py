# Given an int array arr
# If the array is a valid mountain array, return True
    # (A mountain array is one that only increases, reaches a maximum aka peak, then only decreases.) I am assuming that there will only be one peak in this problem, aka a one peak mountain array.

# Declare an int variable = 0
# Sort array with built in python function first, just in case they aren't already sorted (Actually this is really dumb because the problem requires the original order)
# For loop that iterates over each num in the array
    # If statement that checks if a variable is 0
        # if statement that checks if current num is > previous num
            # If it is, continue
            # If it is =, return false
            # If it is less than, use a variable as a flip bit and switch to the other if statement
    # If statement that checks if a variable is 1
        # If statement that checks if current num is < previous num
            # If it is, continue
            # If it is not, return false

# Return true

class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False
        
        flip_bit = 0  # 0 = increasing, 1 = decreasing
        prev_num = arr[0]
        went_up = False
        went_down = False
        
        for i in range(1, len(arr)):
            num = arr[i]
            
            if flip_bit == 0:
                if num > prev_num:
                    went_up = True
                elif num < prev_num:
                    if not went_up:  
                        return False
                    flip_bit = 1
                    went_down = True
                else:
                    return False
            
            elif flip_bit == 1:
                if num < prev_num:
                    went_down = True
                else:
                    return False
            
            prev_num = num
        
        return went_up and went_down
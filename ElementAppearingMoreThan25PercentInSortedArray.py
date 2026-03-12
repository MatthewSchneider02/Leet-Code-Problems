# Given and int array in non decreasing order (ascending but with duplicates)
# There is one int in the array that appears more than 25%
# Return that int


# I'm assuming the most optimal way to do this is with hash maps, as usual with leetcode. I don't have much experience with them yet though so I will need to research this
# Loop through the array
    # If first time seeing the num, add it to the hash map with a value of 1
    # If already in the hash map, increment its value in the hash map by one
# Loop through the hash map
    # For each num divide its' value by the length of the array
#Return the num that has a value > 0.25


# Scratch all that above we can kinda simplify this.
# Logically, if a number appears more than 25% in an array, that means that there will need to be (length_of_array/4 + 1) amount of that num
# Because the array is in non decreasing order, we can just loop through the array, testing to see if the next num is the same as the last
    # If it's the same, increase count
    # If it's different, test to see if count is > length_of_array/4
        # If it is not, reset count and keep looping
        # If it is, return that num

# Looking it up later, it seems there's a cool solution that utilizes the length of the array, and the fact that if a number appears more than 25% it must be found in positions lenght_of_array/4, length_of_array/2, or 3*length_of_array/4.
# for i in range(len(arr) - len(arr)//4):
#    if arr[i] == arr[i + len(arr)//4]:
#        return arr  [i]
# But that's not my solution and I didn't do it that way :)

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        prev_num = arr[0]

        for num in arr:
            if num == prev_num:
                count += 1
            else:
                if count > len(arr)/4:
                    return prev_num
                prev_num = num
                count = 1
                
        if count > len(arr)/4:
            return prev_num

#given an int num
    #if num is even, divide by 2
    #otherwise, subtract one
#return the number of steps to get to 0
    ### I wonder if it's faster to count the number of steps to get to one (then add one step obviously), as each number reaches this stage ###
        ### Or wait, it would be to 2, wouldn't it? Each num will always reach 2, then divide by 2, then reach 1, then subtract 1. Should be more optimal I think##
        #Actually, I think I tried to over optimize it. This doesn't work if num is 1 or 0. Oh well :(
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        count = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                count += 1
            else:
                num -= 1
                count += 1
        return(count)
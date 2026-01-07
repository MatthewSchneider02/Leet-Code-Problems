#i is cust, j is bank
#add all money that a cust has (add all the j values attached to one i value)
#if that is the highest amount so far, replace the max
#return the max

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max_wealth = 0
        for num in accounts:
            current_wealth = 0
            for int in num:
                current_wealth += int
            if current_wealth > max_wealth:
                max_wealth = current_wealth
        return(max_wealth)
        
        #set max_wealth as 0
        #for loop with i
            #set running sum to 0
            #for loop with j
                #add value in account[i][j] to running sum (wealth) for cust
        #if statement, if running sum is greater than max wealth, replace max wealth with running wealth
        #return max_wealth
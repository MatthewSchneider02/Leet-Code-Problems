#given an int n
#loop with i starting at 1 to the int n
    #increment i by one each loop
#return a string array
    #answer[i] will return different string values based on several conditions
        #if i is divisible by 3 and 5: answer[i] == "FizzBuzz"
        #if i is divisible by 3: answer[i] == "Fizz"
        #if i is divisible by 5: answer[i] == "Buzz"
        #if none of the above: answer[i] == "[i]"
#return the string array

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        i = 1
        answer = []
        while i <= n:
            if i % 3 == 0:
                if i % 5 == 0:
                    answer.append(str("FizzBuzz"))
                else:
                    answer.append(str("Fizz"))
            elif i % 5 == 0:
                answer.append(str("Buzz"))
            else:
                answer.append(str(i))
            i += 1

        return(answer)
    


#This is a better solution I discovered, but it's not entirely my own, so I'll leave my own original attempt up top

# class Solution(object):
#     def fizzBuzz(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """

#         i = 1
#         answer = []
#         while i <= n:
#             string = ""
#             if i % 3 == 0:
#                 string += "Fizz"
#             if i % 5 == 0:
#                 string += "Buzz"
#             if string == "":
#                 string += str(i)
#             answer.append(string)
#             i += 1

#         return(answer)
    
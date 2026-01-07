# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Given a list of numbers
#Return the middle num in the list
    #if there are an even number of nums, return the "second" middle node
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mid = head
        end = head

        #This is the correct way to traverse linked lists. Pointers, not iterators.
        #This will loop through the list, with one reaching the end at the same time the other reaches the mid point
        while end and end.next:
            mid = mid.next
            end = end.next.next
        return mid


        #This was my initial thinking, but linked lists are not iterable, so the way I've been solving these easier problems (arrays) won't work here 
        # mid = len(head)/2
        # if len(head) % 2 == 0:
        #     return(head[mid + 1])
        # else:   
        #     return(head[mid])
#Given a root of a binary tree
    #Reads left to right
    #They typically follow this rule:
        #index 0 is root
        #left child node: 2i + 1
        #right child node: 2i + 2
#Inorder traversal is left root, current, right root

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return result
"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_node(self, x):
        if self.left is None:
            self.left = TreeNode(x)
        elif self.right is None:
            self.right = TreeNode(x)
        else:
            if not self.left.insert_node(x):
                self.right.insert_node(x)
        return True


class Solution07:
    def get_height(self, root):
        if root is None:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def is_balanced(self, root):

        if root is None:
            return True

        lh = self.get_height(root.left)
        rh = self.get_height(root.right)

        if abs(lh - rh) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right):
            return True

        return False


if __name__ == "__main__":
    input_s1 = [1, 2, 2, 3, 3, None, None, 4, 4]

    tree1 = TreeNode(input_s1[0])
    tree1.left = TreeNode(input_s1[1])
    tree1.right = TreeNode(input_s1[2])

    tree1.left.left = TreeNode(input_s1[3])
    tree1.left.right = TreeNode(input_s1[4])

    tree1.left.left.left = TreeNode(input_s1[7])
    tree1.left.left.right = TreeNode(input_s1[8])

    s = Solution07()
    print("Input: (%s)" % str(input_s1))
    print("Result: %s" % s.is_balanced(tree1))

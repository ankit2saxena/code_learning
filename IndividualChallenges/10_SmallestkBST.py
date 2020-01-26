class BST:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution10:

    def in_order(self, r):
        return self.in_order(r.left) + [r.val] + self.in_order(r.right) if r else []

    def k_smallest(self, k, tree):
        in_order = self.in_order(tree)

        if None in in_order:
            in_order.remove(None)

        return in_order[k - 1]


if __name__ == "__main__":
    input_s1 = [3, 1, 4, None, 2]
    k = 2

    tree1 = BST(input_s1[0])
    tree1.left = BST(input_s1[1])
    tree1.right = BST(input_s1[2])

    tree1.left.left = BST(input_s1[3])
    tree1.left.right = BST(input_s1[4])

    s = Solution10()
    print("Input: (%s)" % str(input_s1))
    print("Result: %s" % s.k_smallest(k, tree1))

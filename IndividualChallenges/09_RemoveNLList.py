class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert_node(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.insert_node(val)


class Solution09:
    def get_length(self, l):
        l_len = 0

        while l:
            l_len += 1
            l = l.next

        return l_len

    def remove_end_n(self, n, l):
        l_len = self.get_length(l)

        if n == 0:
            return l

        n = l_len - n - 1

        temp_l = ListNode(0)

        for i in range(n):
            temp_l.insert_node(l.val)
            l = l.next

        l.next = l.next.next

        while l:
            temp_l.insert_node(l.val)
            l = l.next

        return temp_l.next


if __name__ == "__main__":
    input_s1 = [1, 2, 3, 3, 5, 3, 3, 2, 1]
    n = 5

    input_list = ListNode(input_s1[0])

    for i in range(1, len(input_s1)):
        input_list.insert_node(input_s1[i])

    s = Solution09()
    print("Input: (%s)" % str(input_s1))

    output_list = s.remove_end_n(n, input_list)
    output_s1 = []

    while output_list:
        output_s1.append(output_list.val)
        output_list = output_list.next

    print("Result: %s" % output_s1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert_node(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.insert_node(val)


class Solution08:
    def get_length(self, l):
        l_len = 0

        while l:
            l_len += 1
            l = l.next

        return l_len

    def is_palindrome(self, l):

        sum = 0
        l_len = self.get_length(l)

        mid = int(l_len / 2)

        if l_len % 2 != 0:
            skip_mid_flag = True
        else:
            skip_mid_flag = False

        ctr = 0
        while ctr < l_len:
            if ctr == mid and skip_mid_flag:
                ctr += 1
                l = l.next
                continue

            if ctr < mid:
                sum += l.val
            else:
                sum -= l.val

            ctr += 1
            l = l.next

        if sum == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    input_s1 = [1, 2, 3, 3, 5, 3, 3, 2, 1]

    input_list = ListNode(input_s1[0])

    for i in range(1, len(input_s1)):
        input_list.insert_node(input_s1[i])

    s = Solution08()
    print("Input: (%s)" % str(input_s1))
    print("Result: %s" % s.is_palindrome(input_list))

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def insert_node(self, val):
        if self.next is None:
            self.next = ListNode(val)
        else:
            self.next.insert_node(val)


class Solution06:
    def merge_lists(self, list1, list2):
        head = list3 = ListNode(0)

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                head.insert_node(list1.val)
                list1 = list1.next
            else:
                head.insert_node(list2.val)
                list2 = list2.next

        while list1:
            head.insert_node(list1.val)
            list1 = list1.next

        while list2:
            head.insert_node(list2.val)
            list2 = list2.next

        return head.next


if __name__ == "__main__":
    input_s1 = [1, 2, 5, 10]
    input_s2 = [2, 3, 4, 6, 8]

    list1 = ListNode(input_s1[0])

    for i in range(1, len(input_s1)):
        list1.insert_node(input_s1[i])

    list2 = ListNode(input_s2[0])

    for j in range(1, len(input_s2)):
        list2.insert_node(input_s2[j])

    s = Solution06()
    print("Input: (%s, %s)" % (input_s1, input_s2))

    merged_list = s.merge_lists(list1, list2)
    output_list = []

    while merged_list:
        output_list.append(merged_list.val)
        merged_list = merged_list.next

    print("Result: %s" % output_list)

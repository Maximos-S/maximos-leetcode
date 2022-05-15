# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        l1_value = []
        l2_value = []
        while l1 != None:
            l1_value.append(str(l1.val))
            l1 = l1.next

        while l2 != None:
            l2_value.append(str(l2.val))
            l2 = l2.next
        l1_value.reverse()
        l2_value.reverse()
        s = ''
        total_sum = list(str(int(s.join(l1_value)) + int(s.join(l2_value))))
        total_sum.reverse()
        result_list_node = ListNode()
        current_result_list_node = result_list_node
        for i in range(len(total_sum) - 1):
            num = total_sum[i]
            current_result_list_node.val = num
            current_result_list_node.next = ListNode()
            current_result_list_node = current_result_list_node.next
        current_result_list_node.val = total_sum[-1]
        return result_list_node

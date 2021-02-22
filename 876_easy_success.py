class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 1
        current_node = head
        while current_node.next:
            length += 1
            current_node = current_node.next
        mid_point = math.ceil(length / 2)
        if length % 2 == 0:
            mid_point = math.ceil(length / 2) + 1
        current_node = head
        for idx in range(mid_point - 1):
            current_node = current_node.next
        return current_node

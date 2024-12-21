class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
        k = k % length

        last_node.next = head
        temp_node = head

        for _ in range(length - k - 1):
            temp_node = temp_node.next
        answer = temp_node.next
        temp_node.next = None
        return answer
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left > right:
            return head
        else:
            hash_map = {}
            i = 1
            #Create a hashmap to store linked list nodes at each position
            while head:
                hash_map[i] = head
                head = head.next
                i += 1
            #reverse the list by swaping the values of the lefest and rightest positions in each iteration 
            while left < right:
                copy = hash_map[left].val
                hash_map[left].val = hash_map[right].val
                hash_map[right].val = copy
                left += 1
                right -= 1
            return hash_map[1]
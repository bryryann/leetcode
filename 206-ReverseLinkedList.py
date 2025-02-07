# Medium
# tags: linked-list, 

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    node = None
    while head:
        t = head.next
        head.next = node
        node = head
        head = t

    return node


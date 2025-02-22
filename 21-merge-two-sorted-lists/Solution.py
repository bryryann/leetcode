# Easy
# Tags: linked-list, recursion

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    hd = ListNode()
    node = hd

    while list1 and list2:
        if list1.val > list2.val:
            node.next = list2
            list2 = list2.next
        else:
            node.next = list1
            list1 = list1.next

        node = node.next

    if list1 or list2:
        node.next = list1 if list1 else list2

    return hd.next



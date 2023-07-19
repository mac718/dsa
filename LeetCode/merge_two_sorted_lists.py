from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    list3 = dummy

    while list1 and list2:
        if list1.val < list2.val:
            list3.next = list1
            list1 = list1.next
        elif list1.val > list2.val:
            list3.next = list2
            list2 = list2.next
        else:
            list3.next = list1
            list1 = list1.next
        list3 = list3.next

    if list1:
        list3.next = list1
    if list2:
        list3.next = list2

    return dummy.next
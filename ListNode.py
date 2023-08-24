class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


Listnode1 = ListNode
ListNode2 = ListNode
ListNode3 = ListNode
ListNode4 = ListNode
head = ListNode
tail = ListNode
Listnode1.next = ListNode2
ListNode2.next = ListNode3

# Next, setting the next pointer for ListNode2 and ListNode3.

ListNode3.next = None

cur = Listnode1
while cur:
    cur = cur.next

# An advantage that Linked Lists have over arrays is that adding a new element can be performed in O(1) time.
# No shifting is required after adding another node and we already have the references to head and tail.
# if we wanted to append a ListNode4 to the end of the list, we would be appending to the tail.

tail.next = ListNode4
tail = ListNode4

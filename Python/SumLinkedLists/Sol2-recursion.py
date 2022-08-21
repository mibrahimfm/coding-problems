# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def insertAtTail(self, x):
        last = self
        while last.next:
            last = last.next
        last.next = ListNode(x)
    
def linkedListToInt(llist, digit=1):
    if llist.next is None:
        return llist.val * digit

    n = llist.val * digit
    return n + linkedListToInt(llist.next, digit*10)
        
def addTwoNumbers(l1, l2):
    n1 = linkedListToInt(l1)
    n2 = linkedListToInt(l2)
    s = n1 + n2
    remainder = 0
    sum_linked_list = None
    while s > 0:
        remainder = s % 10
        s = s // 10
        if sum_linked_list is None:
            sum_linked_list = ListNode(remainder)
        else:
            sum_linked_list.insertAtTail(remainder)

    return sum_linked_list
            

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
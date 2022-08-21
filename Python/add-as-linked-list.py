#Problem:
#Given two linked-lists representing two non-negative integers.
#The digits are stored in reverse order and each of their nodes contain a single digit. 
#Add the two numbers and return it as a linked list.

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
    

def addTwoNumbers(l1, l2):
    n1, n1DigitCounter = 0, 0
    n2, n2DigitCounter = 0, 0
    while l1:
        n1 = n1 + (l1.val * (10 ** n1DigitCounter))
        l1 = l1.next
        n1DigitCounter += 1
    while l2:
        n2 = n2 + (l2.val * (10 ** n2DigitCounter))
        l2 = l2.next
        n2DigitCounter += 1
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
            

l1 = ListNode(6)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l1.next.next.next = ListNode(3)

l2 = ListNode(0)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
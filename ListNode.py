class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

def initList(list):
    if len(list) == 0:
        return None

    head = ListNode(list[0])
    cur = head
    for i in range(1, len(list)):
        cur.next = ListNode(list[i])
        cur = cur.next

    return head

def printList(head):
    cur = head
    while cur != None:
        print(cur)
        cur = cur.next
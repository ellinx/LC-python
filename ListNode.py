class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        ret = []
        cur = self
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return str(ret)

def listNodeList(li):
    """
    :type li: List[int] or List[str]
    :rtype: ListNode
    """
    dummy = ListNode(0)
    cur = dummy
    for each in li:
        cur.next = ListNode(each)
        cur = cur.next
    return dummy.next


# test
if __name__=="__main__":
    head = ListNode(7)
    print(head)
    head = listNodeList([1,2,3,4,5,6])
    print(head)

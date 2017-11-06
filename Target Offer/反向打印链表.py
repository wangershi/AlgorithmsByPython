'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
class ListNode:
    def __init__(self, x=None, next=next):
        self.val = x
        self.next = Next

class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

node3 = ListNode(13)
node2 = ListNode(11, node3)
node1 = ListNode(10, node2)

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))

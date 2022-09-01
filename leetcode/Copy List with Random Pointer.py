class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        map = {}
        head2 = head
        while head:
            map[head] = Node(head.val)
            head = head.next

        ans = map[head2]
        dum = ans
        while dum:
            dum.next = map[head2.next] if head2.next else None
            dum.random = map[head2.random] if head2.random else None
            dum = dum.next
            head2 = head2.next

        return dum

sol = Solution()
sol.copyRandomList()


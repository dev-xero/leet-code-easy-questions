class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        c = 0
        while temp.next != None:
            temp = temp.next
            c += 1
        if c % 2 != 0:
            n = (c // 3)
        else:
            n = c // 2

        for i in range(n):
            head = head.next
            
        return head

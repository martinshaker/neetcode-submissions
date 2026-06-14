# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        col = set()
        col.add(head.val)
        current = head
        print(col)

        while current.next:
            
            print(col)
            if current.next.val in col:
                return True
            if current.next.val not in col:
                col.add(current.next.val)
                print(current.next.val)
                current = current.next
                
                continue
            
            print("current: {}".format(current))
        return False   
        
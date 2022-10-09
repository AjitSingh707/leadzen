class Node:
    def __init__(self,v) -> None:
         self.val = v
         self.next = None

# To find number of onsecutive connected number
def numofsubset(head,nums):
        count = 0
        flag = False
        while head:
            if head.val in nums and not flag:
                count += 1
                flag  = True
            elif head.val not in nums and flag:
                flag = False
            head = head.next
        return count
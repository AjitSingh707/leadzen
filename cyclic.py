class Node:
    def __init__(self,v) -> None:
         self.val = v
         self.next = None
# To check Cycle is present or not
class Cyclic:
    def iscyclic(self,head):
        back = head
        forward = head
        while back and forward and forward.next:
            back = back.next
            forward = forward.next.next
            if back == forward:
                return True
        # addressarr = []
        # while head:
        #     if head in addressarr:
        #         return True 
        #     addressarr.append(head)
        #     head = head.next
        return False






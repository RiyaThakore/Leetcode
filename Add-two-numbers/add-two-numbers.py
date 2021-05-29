class LinkedList:
  def __init__(self,val=0,next=None):
    self.val=val
    self.next=next

class Solution:
  def addTwoNumbers(self, l1, l2):
    curr=LinkedList()
    carry=0
    while l1 and l2:
      if l1 is None:
        if carry!=0:
          add=l2.val+carry
          carry=add//10
          rem=add%10
        else:
          add=l2.val
          carry=add//10
          rem=add%10
        node=LinkedList(rem)
        curr.next=node
        curr=curr.next
        l2=l2.next

      elif l2 is None:
        if carry!=0:
          add=l1.val+carry
          carry=add//10
          rem=add%10
        else:
          add=l1.val
          carry=add//10
          rem=add%10
        node=LinkedList(rem)
        curr.next=node
        curr=curr.next
        l1=l1.next

      else:
        if carry!=0:
          add=l1.val+l2.val+carry
          carry=add//10
          rem=add%10
        else:
          add=l1.val+l2.val
          carry=add//10
          rem=add%10
        node=LinkedList(rem)
        curr.next=node
        curr=curr.next
        l1=l1.next
        l2=l2.next
  return curr

     

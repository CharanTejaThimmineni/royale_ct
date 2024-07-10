# Definition for singly-linked list.

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=0 
        arr=[]
        while head:  
            arr.append(head.val)
            head=head.next
        n=len(arr)    
        for i in arr:
            res=res+i*2**(n-1)
            n=n-1
        return res        
            
            


               
                   

        
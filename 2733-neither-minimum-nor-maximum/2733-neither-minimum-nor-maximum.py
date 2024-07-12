class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
      nums_1=[max(nums),min(nums)]
      nums_2=[]
      for i in nums: 
         if i not in nums_1 and len(nums)>2:
            nums_2.append(i)
            return(nums_2[0])
            
      return -1    
    

     
       



        
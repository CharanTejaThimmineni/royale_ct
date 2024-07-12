class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        
        
        def count(element):
            return nums.count(element)
        
        arr = []
        
        
        for i in nums:
            arr.append(count(i))
        
        for j in arr:
            if j >= 3:
                return False
        
        return True
       
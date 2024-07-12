class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_1=[]
        nums_2=[]
        for i in nums:
            if i not in nums_1:
                nums_1.append(i)
        for k in nums_1:
            nums_2.append(nums.count(k)) 
        max_freq = max(nums_2)      
        j= nums_2.count(max_freq)
        return (j*max_freq)
    
     

    
        
        
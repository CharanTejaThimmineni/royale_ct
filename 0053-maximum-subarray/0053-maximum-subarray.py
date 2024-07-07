class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=0
        for i in nums:
            if currentsum<0:
                currentsum=0
            currentsum+=i  
            maxsum=max(maxsum,currentsum)
        return maxsum      
        
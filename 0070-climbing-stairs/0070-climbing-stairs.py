class Solution:
    def climbStairs(self, n: int) -> int:
        a,b=1,1
        for i in range(n-1):
            nums=a
            a=a+b
            b=nums
        return a    
        
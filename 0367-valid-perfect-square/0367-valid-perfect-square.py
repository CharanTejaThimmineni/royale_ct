class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(num**0.5)==float(num**0.5):
            return True
        return False    
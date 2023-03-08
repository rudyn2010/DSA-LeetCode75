class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set() 
        
        while n not in visited:
            visited.add(n)
            n = self.sumOfSquares(n)
            
            if n == 1:
                return True
            
        return False
    
    def sumOfSquares (self, n: int) -> int:
        
        res = 0
        
        while n:
            
            digit = n % 10
            digit = digit ** 2
            res += digit
            n = n // 10
        
        return res
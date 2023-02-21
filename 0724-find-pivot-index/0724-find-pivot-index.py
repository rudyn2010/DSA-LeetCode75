class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftS = 0
        
        for i in range(len(nums)):
            
            rightS = total - nums[i] - leftS
            
            if leftS == rightS:
                return i
            
            #brute force left to right adds value at each index till we find the pivot index 
            leftS += nums[i]
            
        return -1 
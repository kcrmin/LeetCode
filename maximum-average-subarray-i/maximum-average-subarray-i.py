class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0

        for i in range(k):
            curr += nums[i]
        
        curr /= k
        ans = curr
        
        for i in range(k, len(nums)):
            curr *= k
            curr -= nums[i-k]
            curr += nums[i]
            curr /= k
            
            ans = max(ans, curr)
            
        return ans
        
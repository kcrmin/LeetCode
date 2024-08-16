class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        new_list = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                new_list[i] = nums[right] ** 2
                right -= 1
            else:
                new_list[i] = nums[left] ** 2
                left += 1
        return new_list
            
        
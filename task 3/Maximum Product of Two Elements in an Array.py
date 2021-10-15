class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                maxp = max(maxp, (nums[i]-1)*(nums[j]-1))
        return maxp
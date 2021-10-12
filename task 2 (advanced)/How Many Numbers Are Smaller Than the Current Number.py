from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        smaller_nums = []
        total = 0
        for x,y in sorted(counts.items()):
            total += y
            smaller_nums.append((x,total-y))
        smaller_nums = dict(smaller_nums)
        return [smaller_nums[i] for i in nums]
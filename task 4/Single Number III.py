class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = reduce(lambda acc,n: acc^n,nums,0)
        mask = mask & -mask #only keep LSB of mask
        ret = [0,0]
        for n in nums:
            if n & mask:
                ret[0] = ret[0] ^ n
            else:
                ret[1] = ret[1] ^ n
        return ret
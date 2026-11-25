class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts=Counter(nums)
        c=0
        for num,c in counts.items():
            if c==1:
                return num

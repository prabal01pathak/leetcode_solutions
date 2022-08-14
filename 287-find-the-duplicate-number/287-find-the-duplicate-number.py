class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i, value in enumerate(nums):
            if i == 0:
                prev = value
            else:
                if value == prev:
                    return value
                prev = value
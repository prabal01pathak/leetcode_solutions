from functools import partial

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        for cur in nums:
            output += [[cur]+i for i in output]
        return output

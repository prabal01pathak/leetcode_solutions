class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_hash = {}
        freq = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            result_hash[num] = result_hash.get(num, 0) + 1
        
        for n, c in result_hash.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) -1 , 0, -1):
            if freq[i]:
                for item in freq[i]:
                    res.append(item)
                    if len(res) == k:
                        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:     
        num_freq = Counter(nums)
        sorted_nf = sorted(num_freq.items(), key=lambda num: num[1], reverse = True)
        return [item[0] for item in sorted_nf[:k]]
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)

        longest = 0
        for el in ns:
            if el -1 not in ns:
                count = 1
                while (el + count) in ns:
                    count +=1
                longest = max(count, longest)
        
        return longest
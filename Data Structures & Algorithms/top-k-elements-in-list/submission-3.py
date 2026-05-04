class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        output = []
        for n in nums:
            if n not in map:
                map[n] = 0
            map[n] = map.get(n) + 1
        
        sorted_map = sorted(map.items(), key = lambda x: x[1], reverse = True)
        for key, value in sorted_map[:k]:
                output.append(key)
        
        return output

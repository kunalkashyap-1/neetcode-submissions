class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        map = {}

        for i,s in enumerate(strs):
            sortedStr = "".join(sorted(s))
            if sortedStr not in map:
                map[sortedStr] = []
            map[sortedStr].append(s)
        
        for val in map.values():
            output.append(val)
        
        return output
                
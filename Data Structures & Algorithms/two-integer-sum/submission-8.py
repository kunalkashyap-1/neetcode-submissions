class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i in range(len(nums)):
            map[i] = nums[i]
        
        for i in range(len(nums)):
            diff = target - nums[i]
            for key, value in map.items():
                if value == diff and key != i:
                    return [i, key]
            
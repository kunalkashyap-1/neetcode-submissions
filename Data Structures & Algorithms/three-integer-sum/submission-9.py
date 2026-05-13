class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k-=1
                else:
                    j+=1
        
        return res
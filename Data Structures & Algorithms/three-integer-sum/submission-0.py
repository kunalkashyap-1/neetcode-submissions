class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = len(nums)

        for i in range(l):
            temp = nums[i]
            j = i+1
            k = l-1
            while j<k:
                t1,t2 = nums[j] , nums[k]
                if t1 + t2 == -temp:
                    if [temp,t1 , t2] not in res:
                        res.append([temp,t1 , t2])
                    j+=1
                    k-=1
                elif  t1 + t2 < -temp:
                    j+=1
                else:
                    k-=1
        
        return res
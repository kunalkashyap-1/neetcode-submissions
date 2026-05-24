class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dictq = {}
        l,r = 0,k
        for i in range(len(nums)):
            max_heap = [-x for x in nums[l:r]]
            heapq.heapify(max_heap)
            dictq[i] = max_heap
            l+=1
            r+=1
        
        # print(dictq)
        output = []
        for i in range(len(nums)-k +1):
            output.append(-heapq.heappop(dictq[i]))
        
        return output
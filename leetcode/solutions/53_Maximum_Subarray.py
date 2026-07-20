class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSeen = nums[0]
        total = nums[0] # we assume that 0 isn't the highest has to be nonempty
        n = len(nums)
        for i in range(1, n):
            total = max(total + nums[i], nums[i])
            maxSeen = max(maxSeen, total)
        return maxSeen
class Solution(object):
    def maximumGap(self, nums):
        if len(nums)>=2:
            nums.sort()
            mx=0
            for i in range(1,len(nums)):
                nums[i-1]=nums[i]-nums[i-1]
                mx = max(mx, nums[i-1])
        else:
            return 0
        return mx
        

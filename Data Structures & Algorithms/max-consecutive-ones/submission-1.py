class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        f = 0
        cnt = 0
        for i in range(n):
            if nums[i]==1:
                cnt+=1
            if nums[i]==0:
                cnt=0
            f=max(f,cnt)
        # f = max(f,cnt);
        return f     

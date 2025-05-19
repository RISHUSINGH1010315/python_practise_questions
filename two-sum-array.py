class Solution(object):
    def two_sum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i

        return [] 

sol = Solution()
print(sol.two_sum([2, 7, 11, 15], 9))           

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = -1
        for i in range(len(nums)):
            if (target-nums[i]) in nums:
                if (nums.count(nums[i]) == 1) and (nums[i]==target-nums[i]):
                    continue
                else:    
                    j = nums.index(target-nums[i],i+1)
                    break
        if j>0:
            return [i, j]
        else:
            return []


if __name__ == "__main__":
    print(Solution().twoSum([1,2,3], 3))
    print(Solution().twoSum([2,5,7], 7))

'''
#1493
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

class Solution:
    def longestSubarray(self, nums):
        left = 0
        zeros = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_len = max(max_len, right - left+1)
        return max_len-1
'''
'''
#1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans

'''
'''
class Solution:
    def numSubarraysWithSum(self, nums, goal):
        def atMost(k):
            if k < 0:
                return 0

            left = 0
            total = 0
            currSum = 0

            for right in range(len(nums)):
                currSum += nums[right]

                while currSum > k:
                    currSum -= nums[left]
                    left += 1

                total += right - left + 1

            return total

        return atMost(goal) - atMost(goal - 1)
'''
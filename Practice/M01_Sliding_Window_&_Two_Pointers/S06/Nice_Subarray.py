'''
#1248 
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def sub_arr(k):
            if k < 0:
                return 0
            left, count ,odd = 0,0,0
            for right in range(len(nums)):
                if nums[right]%2 == 1:
                    odd += 1
                while odd > k:
                    if nums[left]%2 == 1:
                        odd -= 1
                    left += 1
                count += (right - left + 1)
            return count 
        return sub_arr(k) - sub_arr(k-1)

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

    
#1763
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        char_set = set(s)
        for i,char in enumerate(s):
            if char.swapcase() not in char_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                return left if len(left) >= len(right) else right
        return s
#523
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            remainder = running_sum % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i  
        return False

'''
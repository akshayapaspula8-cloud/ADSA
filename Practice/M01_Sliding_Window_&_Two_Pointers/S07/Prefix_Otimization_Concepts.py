'''
#1480
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        current_sum = 0
        
        for num in nums:
            current_sum += num
            result.append(current_sum)
            
        return result
#1732 
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_alt = 0
        max_alt = 0
        
        for g in gain:
            curr_alt += g
            max_alt = max(max_alt, curr_alt)
            
        return max_alt
#1991
class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
            
        return -1
#724
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # right_sum = total_sum - left_sum - num
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
            
        return -1

#523


'''
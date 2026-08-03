
'''#26[leetcode problem]
from typing import List
def removeDuplicates(nums: List[int]) -> int:

        k=0
        for i in range(1,len(nums)):
            if nums[k] != nums[i]:
               
                k+=1
                nums[k] = nums[i]
                
        return k + 1
nums=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
#27
def removeElement(self, nums: List[int], val: int) -> int:   
    i=0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i
nums=[3,2,2,3]
val=3
print(removeElement(nums,val))   
#167
def twoSum(numbers: List[int], target: int) -> List[int]:
    left,right =0,len(numbers)-1
    while left<right:
        c_s=numbers[left]+numbers[right]
        if c_s ==target:
            return [left+1,right+1]
        elif c_s<target:
            left+=1
        else:
            right-=1     
numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))
#977
'''
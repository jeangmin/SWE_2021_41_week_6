from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
# YOUR ANSWER
  for i in range(len(nums)):
    for j in range(len(nums)):
      if i==j:
        continue
      else:
          if nums[i]+nums[j]==target:
            return [i, j]
          
  return 

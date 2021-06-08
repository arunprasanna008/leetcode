"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from verification import verify

class Solution:

    def twoSum_1(self, nums, target, expected_output):
        """
        using enumerate:
        enumerate iterates the values of a list with its index
        """
        actual_output = []
        for index, num in enumerate(nums):
            if (target-num) in nums and nums.index(target-num) != index:
                actual_output = [nums.index(target-num), index]
                actual_output.sort()
                verify(actual_output,expected_output)
                break
            else:
                if index == (len(nums)-1):
                    print("The sum of any two items from the list %s won't make the target %s" %(nums,target))
                
            
        
my_object = Solution()
my_object.twoSum_1(nums=[2,7,3],target=5,expected_output=[0,2])
my_object.twoSum_1(nums=[3,4],target=7,expected_output=[0,1])
my_object.twoSum_1(nums=[3,6,9,1,2,4],target=7,expected_output=[0,5])
my_object.twoSum_1(nums=[3,4,1,1,1,3,2],target=6,expected_output=[1,6])
my_object.twoSum_1(nums=[3,3,1,1,1,1,1,3,2],target=6,expected_output=[0,1])
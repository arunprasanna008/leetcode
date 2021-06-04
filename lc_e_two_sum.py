def verify(actual_output, expected_output):
    try:
        assert (actual_output == expected_output)
        print("correct solution %s" % actual_output)
    except AssertionError:
        print ("wrong solution \n actual: %s \n expected: %s" % (actual_output, expected_output))

class Solution:
    def twoSum(self, nums, target, expected_output):
        actual_output = []
        for index, num in enumerate(nums):
            if (target-num) in nums and nums.index(target-num) != index:
                if nums.index(target-num) > index:
                    actual_output = [index, nums.index(target-num)]
                else:
                    actual_output = [nums.index(target-num), index]
                verify(actual_output,expected_output)
                break
            else:
                if index == (len(nums)-1):
                    print("The sum of any two items from the list %s won't make the target %s" %(nums,target))
                
            
        
my_object = Solution()
my_object.twoSum(nums=[2,7,3],target=5,expected_output=[0,2])
my_object.twoSum(nums=[3,4],target=7,expected_output=[0,1])
my_object.twoSum(nums=[3,6,9,1,2,4],target=7,expected_output=[0,5])
my_object.twoSum(nums=[3,4,1,1,1,3,2],target=6,expected_output=[1,6])
my_object.twoSum(nums=[3,3,1,1,1,1,1,3,2],target=6,expected_output=[0,1])
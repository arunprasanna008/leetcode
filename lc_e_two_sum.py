def verify(actual_output, expected_output):
        try:
            assert (actual_output == expected_output)
        except AssertionError:
            print ("wrong answer")

class Solution:
    def twosum(self, nums, target, expected_output):
        print(nums, target)
        for index, num in enumerate(nums):
            print(index, num, expected_output)
            v = [1,1]
        verify(v,expected_output)
            
        
my_object = Solution()
my_object.twosum(['2','7','3'],9,[0,1])
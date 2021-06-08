"""
The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.

For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

"""
from verification import verify

def get_key(val,numVal):
    for key, value in numVal.items():
         if val == value:
             return str(key)

def create_map():
        numVal = {}
        accepted_values = ['a','b','c','d','e','f','g','h','i','j']
        i = 0
        for item in accepted_values:
            numVal[i] = item
            i = i+1
        return numVal
             
class Solution:
    def __init__(self):
        self.numVal = create_map()
   
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str, expected_output) -> bool:
        firstWord_Total = self.find_total(firstWord)
        secondWord_Total = self.find_total(secondWord)
        targetWord_Total = self.find_total(targetWord)
        if int(firstWord_Total) + int(secondWord_Total) == int(targetWord_Total):
            verify('True',expected_output)
        else:
            verify('False',expected_output)
       
    def find_total(self,string):
        total = ''
        for item in string:
            total  += get_key(item,self.numVal)
        return total
        
my_obj = Solution()
my_obj.isSumEqual('j','j','bi','True')
my_obj.isSumEqual('aaaa','aa','a','True')
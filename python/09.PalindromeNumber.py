#we have to show the if a number is palindrome, we use to strings of x to compare our integer and the integer from it's tail to it's head

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

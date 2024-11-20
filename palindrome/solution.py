class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else str(x) == str(x)[::-1] 

if __name__ == "__main__":
    sol = Solution()

    assert sol.isPalindrome(121) == True, "Failed #1"
    assert sol.isPalindrome(-121) == False, "Failed #2"
    assert sol.isPalindrome(10) == False, "Failed #3"

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle) == 1 and haystack[0] == needle):
            return 0

        for i in range(len(haystack)):
            batch = haystack[i:i+len(needle)]
            if(len(batch) < len(needle)):
                break
            if(batch == needle):
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad") == 0, "Failed #1"
    assert sol.strStr("leetcode", "leeto") == -1, "Failed #2"


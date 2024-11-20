from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
             return strs[0]

        base = strs[0]
        longest_prefix = ""
    
        tmp_prefix = ""
        stop_prefix = False
        for char in base:
            tmp_prefix += char
            
            for string in strs[1:]:
                if(not string.startswith(tmp_prefix)):
                    stop_prefix = True
                    break

            if(stop_prefix):
                break
            
            longest_prefix += char



        return longest_prefix


if __name__ == "__main__":
    sol = Solution()

    assert sol.longestCommonPrefix(["flower","flow","flight"]) == "fl", "Failed #1"
    assert sol.longestCommonPrefix(["dog","racecar","car"]) == "", "Failed #2"
    assert sol.longestCommonPrefix(["dog"]) == "dog", "Failed #3"

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if(len(nums) <= 1):
            return len(nums)

        visited = []
        remaped_area = 0
        for i in range(len(nums)):
            actual = nums[i]
            
            if(actual not in visited):
                visited.append(actual)
            elif(i == len(nums)-1 or i == len(nums) - remaped_area - 1):
                break
            else:

                ptr = i+1
                while nums[ptr] == actual and ptr < len(nums)-1:
                    ptr += 1

                remaped_area += ptr-i
                if(nums[ptr] != actual and nums[ptr] not in visited):
                    visited.append(nums[ptr])

                nums = [*nums[0:i], *nums[ptr:], *nums[i:ptr]]
        
        return len(visited)

if __name__ == "__main__":
    sol = Solution()
    assert sol.removeDuplicates([1,1,2]) == 2, "Failed #1"
    assert sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5, "Failed #2"

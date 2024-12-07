from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target > nums[-1]):
            return len(nums)
        elif(target == nums[-1]):
            return len(nums)-1
        elif(target <= nums[0]):
            return 0

        get_index = lambda i_min, i_max : (i_min+i_max)//2

        index = (len(nums)-1)//2
        index_max = len(nums)-1
        index_min = 0

        while index_max != index_min:
            if(nums[index] == target):
                return index
            
            if(target < nums[index]):
                index_max = index
            elif(target > nums[index]):
                index_min = index+1
            index = get_index(index_min, index_max)
            

        if(nums[index] < target):
            return index+1
        return index

if __name__ == "__main__":
    sol = Solution()

    assert sol.searchInsert([1,3,5,6], 5) == 2, "Failed #1"
    assert sol.searchInsert([1,3,5,6], 2) == 1, "Failed #2"
    assert sol.searchInsert([1,3,5,6], 7) == 4, "Failed #3"
    assert sol.searchInsert([1,2,4,6,8,9,10], 10) == 6, "Failed #4"
    assert sol.searchInsert([2,3,5,6,9],7) == 4, "Failed #5"
    assert sol.searchInsert([3,5,7,9,10],8) == 3, "Failed #6"

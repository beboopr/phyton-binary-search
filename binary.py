# binary search

from typing import List

def search(nums: List[int], target: int) -> int:
    length = len(nums) -1
    low, high = 0, length

    while low <= high:
        mid = (low +high) // 2 #3

        if nums[mid] == target: # 15==30
            return mid
        elif nums[mid] < target: # 15 > 30
            high = mid -1 # high = 3-1 = 2
        else:
            low = mid + 1
        return -1
print(search([1,7,10,15,30,40],7))
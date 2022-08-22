#LeetCode 704. Binary Search
# Easy
#Solution 1

nums = [-1,0,3,5,9,12] 
target = 9

def search(nums, target):
    low = 0 
    high = len(nums)-1
    while low <= high:
        mid = (low + high)
        guess = nums[mid]
        if guess == target:
            return mid
        if target < guess:
            high = mid - 1
        else:
            low = mid + 1
    return -1
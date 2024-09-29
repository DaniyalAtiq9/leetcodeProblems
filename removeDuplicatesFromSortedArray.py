# In this section, I solved LeetCode 26. Remove Duplicates from Sorted Array. The problem statement reads as:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each
# unique element appears only once. The relative order of the elements should be kept the same. Then return the number of
# unique elements in nums. Consider the number of unique elements of nums to be k, to get accepted, you need to do the
# following things:
# i.) Change the array nums such that the first k elements of nums contain the unique elements in the order they were
# present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# ii.) Return k.
# Example: Input: nums = [1,1,2] Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
def removeDuplicates(nums):
    # Finding the length of original array
    # if length is 1 simply return
    n = len(nums)
    if n <= 1:
        return n
    # Othewise, create a pointer that starts at 1
    idx = 1
    # The loop will iterate n times
    for i in range(1, n):
        # If the element at index 0 and index 1 are not same, store that element at index 0 and so on
        if nums[i] != nums[i - 1]:
            nums[idx] = nums[i]
            # Increment the index pointer each time it does that
            idx += 1
    # Return the index pointer which will be equal to the number of distinct elements in that array
    return idx

# There's a code for custom judge that will check your solution. I have included it in main function
if __name__ == "__main__":
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expectedArr = [0, 1, 2, 3, 4]  # Expected result after removing duplicates
    k = removeDuplicates(arr)

    assert k == len(expectedArr), "Length mismatch"
    for i in range(k):
        assert arr[i] == expectedArr[i], f"Mismatch at index {i}"

    # print the result
    print("Array after removing duplicates:")
    for i in range(k):
        print(arr[i], end=" ")
# This solution uses 0(n) time since the loop iterates  n times and the space complexity is O(1) since the removing
# of duplicates is in-place.
# Thoughts:
# I found the description of this problem slightly confusing especially the rules regarding k.
# My aim was to find the simplest solution I could think of and it worked so you should also try the simplest solution
# that comes to your mind.

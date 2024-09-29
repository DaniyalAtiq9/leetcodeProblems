# In this section, I solved LeetCode # 88 "Merge Sorted Array". The problem statement reads as:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array
# sorted in non-decreasing order
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
def merge(nums1, m, nums2, n):
    """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # three pointers i, j and k
    i = m - 1 # last valid element in nums1
    j = n - 1 # last valid element in nums2
    k = m + n -1 # last element (which is 0) in nums1
    # iterate in reverse order and compare elements of num1 and num2
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            # if nums1[i] > nums2[j] then only i will be decremented
            # and j will remain the same, meaning that if this condition is true and i,j = 2, then after
            # this statement i = 1 and j = 2
            i = i - 1
        else:
            nums1[k] = nums2[j]
            # same as here
            j = j -1
        k = k - 1
    # if nums2 still has elements present not copied in nums1,
    # e.g: nums1 = [7,11,23,0,0,0] and nums2 = [2,5,6] then elements of nums2 will be copied here
    while j >= 0:
        nums1[k] = nums2[j]
        j = j - 1
        k = k - 1
            
# provided main function so you can test on your IDE
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
# The time complexity of this code is O(m + n), and space complexity is 0(1) since the sorting is in-place.



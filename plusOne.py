# In this section, I solved LeetCode # 66. "Plus One". The description reads as:
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least  significant in left-to-right order. The large integer does
# not contain any leading 0's. Increment the large integer by one and return the resulting  array of digits.
# Example:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
def plusOne(digits):
    # Get the size of array
    n = len(digits)
    # Maintain a pointer that points to the last element
    ptr = n - 1
    # Iterate till n
    for i in range(0, n):
        # If the last element is 9, adding 1 will give us 10
        # and we have to take care of the carrying
        if digits[ptr] + 1 == 10:
            digits[ptr] = 0
            # Decrement ptr each time it happens
            ptr = ptr - 1
        # Otherwise, simply add 1 to the number and return the 
        # array since, no carrying takes place
        else:
            digits[ptr] = digits[ptr] + 1
            return digits
    # If an array has elements [9,9,9] adding 1 will give us
    # [1,0,0,0], so we have to take care of the extra 1 at the
    # beginning of array. We can do this by list concatenation
    return [1] + digits
    
# For convenience, I have added a main function so you first test on your own IDE and then proceed to LeetCode
if __name__ == "__main__":
    #num = [4,3,2,1]
    #num = [1,2,3]
    num = [9]
    result = plusOne(num)
    print(result)
# The time complexity of this code is O(n) since the loop n times and space complexity is 0(1), since no extra space
# is used.

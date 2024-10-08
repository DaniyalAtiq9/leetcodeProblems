# I solved LeetCode # 70. "Climbing Stairs". The problem statement reads as:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# I have taken a custom input for no. of stairs. This is a dynamic programming problem, and the hint here is
# fibonacci sequence. P.S. Try to draw a diagram of stairs to better understand it.
def climbStairs(n):
    # if no. of stairs = 1, then only 1 combination to climb them
    if n == 1:
        return 1
    # if no. of stairs = 2, then only 2 combination to climb them
    elif n == 2:
        return 2
    # We know the combinations to climb 1 and 2 stairs.
    prev2 = 1 # This is for one stair
    prev1 = 2 # This is for two stairs
    # The no. of combinations to climb let's say 3 stairs is equal to the sum of number of combinations present to climb 1
    # stair hence  arr[i - 1] and no. of combinations available to climb 2 stairs hence arr[i - 2], this is true for *n* no.
    # of stairs
    for i in range(3,n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1

# Main function written for convenience
if __name__ == "__main__":
    n = int(input("Enter number of stairs: "))
    result = climbStairs(n)
    print(f"No. of ways to climb {n} stairs: {result}")

# My original solution had O(n) time and space complexity, however I found out that I could also do this problem
# in O(1) complexity, hence I edited it. My previous solution used an array for memoization which took O(n) space.


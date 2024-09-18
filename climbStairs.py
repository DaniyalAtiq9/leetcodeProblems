# I solved leetcode 70. Climbing Stairs problem
# The problem statement reads as:
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# I have taken a custom input for no. of stairs.
def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    arr = [0] * (n + 1)
    arr[1] = 1
    arr[2] = 2
    for i in range(3,n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]


if __name__ == "__main__":
    n = int(input("Enter number of stairs: "))
    result = climbStairs(n)
    print(f"No. of ways to climb {n} stairs: {result}")


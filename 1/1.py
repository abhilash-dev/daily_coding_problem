'''
Question:

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def has_sum(arr, k):
    arr = sorted(arr)
    left = 0
    right = len(arr) - 1

    while (left <= right):
        sum = arr[left] + arr[right]

        if sum == k:
            return True

        if sum > k:
            right -= 1

        if sum < k:
            left += 1
    return False


print(has_sum([10, 15, 3, 7], 17))
print(has_sum([10, 15, 3, 7], 11))
print(has_sum([10, 15, 3, 7], 3))
print(has_sum([10, 15, 3, 7], 18))
print(has_sum([3, -5, 2, 1], -3))

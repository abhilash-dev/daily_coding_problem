'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates
and negative numbers as well. For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
'''


# N Log N solution
def first_missing_positive(arr):
    if not arr:
        return 1
    else:
        arr = sorted(arr)
        size = len(arr)
        for i in range(size - 1):
            if arr[i] > 0 and arr[i + 1] - arr[i] > 1:
                return arr[i] + 1

        if arr[size - 1] < 1:
            return 1
        else:
            return arr[size - 1] + 1


print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([]))
print(first_missing_positive([-3, -5, -2, -2]))

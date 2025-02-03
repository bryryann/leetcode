# Easy
# Tags: array, two-pointers

def remove_element(nums: list[int], val: int) -> int:
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


print(remove_element([3, 2, 2, 3], 3)) # k=2, nums=[2, 2, _, _]
print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2)) # k=5, nums=[0, 1, 3, 0, 4, _, _]

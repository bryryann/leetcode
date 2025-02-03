# Easy
# Tags: array, two-pointer

def remove_duplicates(nums: list[int]) -> int:
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k


print(remove_duplicates([1, 1, 2])) # k=2, nums=[1, 2, _]
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])) # k=5, nums=[0, 1, 2, 3, 4, _, _, _, _, _]
print(remove_duplicates([1])) # k=1, nums=[1]

# Easy
# Tags: array, hash table, sorting

def containsDuplicate(nums: list[int]) -> bool:
    table = set()

    for n in nums:
        if n in table:
            return True
        table.add(n)

    return False


print(containsDuplicate([1, 2, 3, 1])) # true
print(containsDuplicate([1, 2, 3, 4])) # false
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])) # true

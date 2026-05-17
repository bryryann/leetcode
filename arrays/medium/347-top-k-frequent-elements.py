# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.

from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count = {}

    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1

    return [k for k, _ in sorted(
        count.items(),
        key=lambda item: item[1],
        reverse=True
    )][:k]

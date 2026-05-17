# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from typing import List, Dict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams: Dict[str, List[str]] = {}

    for st in strs:
        s = str(sorted(st))

        if s in anagrams:
            anagrams[s].append(st)
        else:
            anagrams[s] = [st]

    return list(anagrams.values())

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}

    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    for c in t:
        if c not in count or count[c] == 0:
            return False

        count[c] -= 1

    return True

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#include <algorithm>
#include <iostream>
#include <unordered_map>

bool is_anagram(std::string s, std::string t) {
    if (s.length() != t.length())
        return false;

    std::unordered_map<char, int> count;

    for (char c : s) {
        if (count.find(c) != count.end()) {
            count[c] += 1;
        }
        else {
            count.insert({c, 1});
        }
    }

    for (char c : t) {
        if (count.find(c) == count.end() || count[c] == 0)
            return false;

        count[c] -= 1;
    }

    return true;
}

// Given an array of integers 'nums' and an integer 'target', 
//  return indices of the two numbers such that they add up to 'target'.

//  You may assume that each input would have exactly one solution, and you may not use the same element twice.

#include <vector>
#include <unordered_map>

std::vector<int> two_sum(std::vector<int>& nums, int target) {
    std::unordered_map<int, int> map;

    for (int i = 0; i < nums.size(); ++i) {
        int rem = target - nums[i];

        if (map.find(rem) != map.end()) {
            return {map[rem], i};
        }

        map[nums[i]] = i;
    }

    return {};
}

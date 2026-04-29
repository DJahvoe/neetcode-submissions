class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let numToIndex = {};

        for (let i = 0; i < nums.length; i++) {
            let complement = target - nums[i];

            if (numToIndex.hasOwnProperty(complement)) {
                return [numToIndex[complement], i];
            }

            numToIndex[nums[i]] = i;
        }
        
        return [];
    }
}

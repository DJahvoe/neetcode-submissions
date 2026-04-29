class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const frequencyMap = new Map();

        nums.forEach((num) => {
            frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
        });

        const sorted = [...frequencyMap.entries()].sort((a, b) => b[1] - a[1]);
        
        return sorted.slice(0, k).map(([num]) => num);
    }
}

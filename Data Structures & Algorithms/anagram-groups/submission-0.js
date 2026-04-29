class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = {};

        for (let str of strs) {
            // Sort the string to generate the key
            let key = str.split('').sort().join('');

            // Initialize the group if it doesn't exist
            if (!map[key]) {
                map[key] = [];
            }

            // Add the string to the group
            map[key].push(str);
        }

        // Return the grouped anagrams
        return Object.values(map);
    }
}

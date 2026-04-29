class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let output = [];
        for(let i = 0; i < nums.length; i++)
        {
            let left = 1;
            let right = 1;

            for(let j = 0; j < nums.length; j++)
            {
                if(i == j) continue;
                if(j < i) {
                    left *= nums[j];
                }
                else {
                    right *= nums[j];
                }
            }

            output.push(left * right);
        }
        return output;
    }
}

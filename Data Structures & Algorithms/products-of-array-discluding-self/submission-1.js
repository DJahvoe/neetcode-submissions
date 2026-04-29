class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prefix = [];
        let postfix = [];
        let result = [];

        let temp = 1;
        for(let i = 0; i < nums.length; i++)
        {
            temp *= nums[i];
            prefix[i] = temp;
        }
        temp = 1;
        for(let i = nums.length - 1; i >= 0; i--)
        {
            temp *= nums[i];
            postfix[i] = temp;
        }
        
        // Result
        for(let i = 0; i < nums.length; i++)
        {
            let left = (i - 1) < 0 ? 1 : prefix[i - 1];
            let right = (i + 1) == nums.length ? 1 : postfix[i + 1];
            result[i] = left * right;
        }
        console.log(prefix);
        console.log(postfix);
        console.log(result);

        return result;
    }
}

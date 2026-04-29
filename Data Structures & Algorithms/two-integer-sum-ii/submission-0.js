class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let leftP = 0;
        let rightP = numbers.length - 1;

        while(leftP != rightP)
        {
            let sum = numbers[leftP] + numbers[rightP];
            if(sum < target)
            {
                leftP++;
            }
            else if(sum > target)
            {
                rightP--;
            }
            else
            {
                return [leftP + 1, rightP + 1];
            }
        }
    }
}

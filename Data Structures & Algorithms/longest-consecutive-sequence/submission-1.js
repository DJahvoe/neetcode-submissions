class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */ 
    longestConsecutive(nums) {
        if(nums.length == 0) return 0;
        let uniqueNums = [...new Set(nums)];
        // sort
        for(let i = 0; i < uniqueNums.length; i++)
        {
            for(let j = i; j < uniqueNums.length; j++)
            {
                if(uniqueNums[i] > uniqueNums[j])
                {
                    let temp = uniqueNums[i];
                    uniqueNums[i] = uniqueNums[j];
                    uniqueNums[j] = temp;
                }
            }
        }
        // assess
        let longest = 1;
        let tempLength = 1;
        for(let i = 0; i < uniqueNums.length - 1; i++)
        {
            if(uniqueNums[i] + 1 == uniqueNums[i+1])
            {
                tempLength++;
            }
            else
            {
                tempLength = 1;
            }

            if(longest < tempLength)
            {
                longest = tempLength;
            }
        }
        return longest;
    }
}

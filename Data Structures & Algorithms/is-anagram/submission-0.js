class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let firstSet = {};
        let secondSet = {};

        for(let tempS of s)
        {
            if(tempS in firstSet)
            {
                firstSet[tempS]++;
            }
            else
            {
                firstSet[tempS] = 0;
            }
        }

        for(let tempT of t)
        {
            if(tempT in secondSet)
            {
                secondSet[tempT]++;
            }
            else
            {
                secondSet[tempT] = 0;
            }
        }

        for(let key in firstSet)
        {
            if(!(firstSet[key] == secondSet[key])) {
                return false;
            }
        }

        for(let key in secondSet)
        {
            if(!(firstSet[key] == secondSet[key])) {
                return false;
            }
        }
        return true;
    }
}

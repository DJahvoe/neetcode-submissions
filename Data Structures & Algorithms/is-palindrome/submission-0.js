class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.replace(/[^\w]+/g,"").toLowerCase();
        let firstBunny = 0;
        let secondBunny = s.length - 1;
        while(firstBunny < secondBunny)
        {
            if(s[firstBunny] != s[secondBunny])
            {
                return false;
            }
            firstBunny++;
            secondBunny--;
        }
        return true;
    }
}

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = [];
        for(let i = 0; i < s.length; i++)
        {
            if(s[i] == '[' || s[i] == '{' || s[i] == '(')
            {
                stack.push(s[i])
            }
            else
            {
                let lastEl = stack.pop();
                let combination = lastEl + s[i];
                console.log(stack);
                console.log(combination);
                if(combination != '{}' && combination != '[]' && combination != '()')
                {
                    return false;
                }
            }
            
        }

        if(stack.length != 0) return false;
        return true;
    }
}

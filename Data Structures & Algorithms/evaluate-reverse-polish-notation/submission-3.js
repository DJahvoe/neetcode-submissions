class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        let stack = [];
        for(let i = 0; i < tokens.length; i++)
        {
            let first, second;
            switch(tokens[i]){
                case "+":
                    first = stack.pop();
                    second = stack.pop();
                    stack.push(second + first);
                    break;
                case "-":
                    first = stack.pop();
                    second = stack.pop();
                    stack.push(second - first);
                    break;
                case "*":
                    first = stack.pop();
                    second = stack.pop();
                    stack.push(second * first);
                    break;
                case "/":
                    first = stack.pop();
                    second = stack.pop();
                    stack.push(Math.trunc(second / first));
                    break;
                default:
                    stack.push(+tokens[i]);
            }
            console.log(stack);
        }
        return stack.pop();
    }
}

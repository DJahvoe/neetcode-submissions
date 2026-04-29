class Solution {
    isHorizontalValid(board) {
        for(let i = 0; i < board.length; i++)
        {
            let horizontalMap = {};
            let horizontalLine = board[i];
            for(let j = 0; j < horizontalLine.length; j++)
            {
                let num = horizontalLine[j];
                if(num == ".") continue;

                if(horizontalMap[num] != null)
                {
                    console.log("Horizontal Invalid");
                    return false;
                }
                else
                {
                    horizontalMap[num] = 1;
                }
            }
        }
        console.log("Horizontal Valid");
        return true;
    }

    isVerticalValid(board) {
        for(let i = 0; i < board.length; i++)
        {
            let verticalMap = {};
            for(let j = 0; j < board.length; j++)
            {
                let num = board[j][i];
                if(num == ".") continue;

                if(verticalMap[num] != null)
                {
                    console.log("Vertical Invalid");
                    return false;
                }
                else
                {
                    verticalMap[num] = 1;
                }
            }
        }
        console.log("Vertical Valid");
        return true;
    }

    isSquareValid(board) {
        for(let l = 0; l < board.length; l += 3)
        {
            for(let i = 0; i < board.length; i += 3)
            {
                let squareMap = {};
                for(let j = l; j < l+3; j++)
                {
                    for(let k = i; k < i+3; k++)
                    {
                        let num = board[j][k];
                        if(num == ".") continue;

                        if(squareMap[num] != null)
                        {
                            console.log("Square Invalid");
                            return false;
                        }
                        else
                        {
                            squareMap[num] = 1;
                        }
                    }
                }
            }
        }
        console.log("Square Valid");
        return true;
    }
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        console.log(board);
        if(!this.isHorizontalValid(board)) return false;
        if(!this.isVerticalValid(board)) return false;
        if(!this.isSquareValid(board)) return false;
        return true;
    }
}

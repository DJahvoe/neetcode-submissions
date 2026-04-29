class MinStack {
    constructor() {
        this.arr = [];
        this.head = -1;
        this.minVal = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.head++;
        this.arr[this.head] = val;
        if(this.head == 0)
        {
            this.minVal[this.head] = val;
        }
        else
        {
            this.minVal[this.head] = 
                this.minVal[this.head - 1] > val ? val : this.minVal[this.head - 1];
        }
    }

    /**
     * @return {void}
     */
    pop() {
        this.head--;
    }

    /**
     * @return {number}
     */
    top() {
        return this.arr[this.head];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minVal[this.head];
    }
}

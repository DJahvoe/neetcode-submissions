class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        print("PUSH")
        if self.length == self.capacity:
            self.resize()

        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1
        print(self.arr)


    def popback(self) -> int:
        print("POP")
        top = self.arr[self.length - 1]
        self.length -= 1

        return top
 

    def resize(self) -> None:
        print("RESIZE")
        # Create new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

        # Copy the elements to new array
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity

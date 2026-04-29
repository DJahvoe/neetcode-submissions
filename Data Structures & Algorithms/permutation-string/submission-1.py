class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        charCount = {}
        for char in s1:
            if not char in charCount:
                charCount[char] = 0
            charCount[char] += 1
        
        l = 0
        currentCount = {}
        for r in range(len(s2)):
            print(l, r)
            # slide window
            if r - l + 1 > len(s1):
                print("geser")
                currentCount[s2[l]] -= 1
                if currentCount[s2[l]] <= 0:
                    del currentCount[s2[l]]
                l += 1
            if not s2[r] in currentCount:
                currentCount[s2[r]] = 0
            currentCount[s2[r]] += 1
            r += 1

            # skip if not equal length
            if len(currentCount) != len(charCount):
                continue
            # check if all currentCount equal to charCount
            for char in currentCount:
                print(char)
                currentEl = currentCount[char]
                charEl = charCount[char] if char in charCount else -1
                if not (currentEl == charEl):
                    break
            else:
                return True
        return False
                
        

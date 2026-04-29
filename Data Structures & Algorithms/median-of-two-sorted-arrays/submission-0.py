class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        total =  len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1
        while True:
            print("itr")
            i = (l + r) // 2
            j = half - i - 2
            print(i)
            print(j)

            Aleft = A[i] if i >= 0 else float("-infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Aright = A[i + 1] if i + 1 < len(A) else float("infinity")
            Bright = B[j + 1] if j + 1 < len(B) else float("infinity")
            print(Aleft, Aright, Bleft, Bright)
            if(Aleft <= Bright and Bleft <= Aright):
                if total % 2 == 0:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
                else:
                    return min(Aright, Bright)
            elif Bleft > Aright:
                l = i + 1
            else:
                r = i - 1

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2

    if len(A) > len(B):
        A, B = B, A
    
    total = len(A) + len(B) 
    half = total // 2
    # Converting to 0-indexed value
    half = half - 1 


    l, r = 0, len(A) - 1

    while True:
        m = (l + r) // 2
        n = half - m - 1

        if m >= 0:
            Aleft = A[m]
        else:
            Aleft = float("-infinity")
        
        if m + 1 < len(A):
            Aright = A[m + 1]
        else:
            Aright = float("infinity")
        
        if n >= 0:
            Bleft = B[n]
        else:
            Bleft = float("-infinity")
        
        if n + 1 < len(B):
            Bright = B[n + 1]
        else:
            Bright = float("infinity")

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            else:
                return ((max(Aleft, Bleft) + min(Aright, Bright)) / 2)    
        elif Aleft > Bright:
            r = m - 1
        else:
            l = m + 1

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # Ensure A is the smaller array to minimize the binary search range
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2       # Partition index for A
            j = half - i - 2       # Partition index for B

            # Handle out-of-bound edge cases using infinity
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Check if partition is valid: all left elements <= all right elements
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements: the median is the smallest element of the right partition
                if total % 2:
                    return min(Aright, Bright)
                # Even total elements: average of max(left) and min(right)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # Too many elements taken from A
                r = i - 1
            else:
                # Too few elements taken from A
                l = i + 1
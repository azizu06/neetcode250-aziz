class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, l, r):
            if l < r:
                m = l+(r-l)//2
                mergeSort(nums, l, m)
                mergeSort(nums, m+1, r)
                merge(nums, l, m, r)
        
        def merge(nums, l, m, r):
            left = nums[l:m+1]
            right = nums[m+1:r+1]

            i,j,k = 0,0,l
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i+=1
                    k+=1
                else:
                    nums[k] = right[j]
                    j+=1
                    k+=1

            while i < len(left):
                nums[k] = left[i]
                i+=1
                k+=1

            while j < len(right):
                nums[k] = right[j]
                j+=1
                k+=1
        mergeSort(nums, 0, len(nums)-1)
        return nums
                
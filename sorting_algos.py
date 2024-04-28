"""

Insertion sort: In place sorting. fist element is sorted, then consider every next element, if sorted element is greater,
than the next element then move to forward. After all the elements of the sorted part are moved one further,
we have space to insert the current element. 

Selection sort: In place sorting. Hold the first index, then iterate through the remaining array (arr[i+1, len(arr)),
once you find the smallest element, swap it with the first/current element in the outer loop. 

Worst Case: O(n^2)
Best Case: O(n^2)


Quick sort: Divide and conquer algorithm. Find a pivot by calling the helper function partition(arr, left, right). 
Partition chooses the right most element as pivot, then rearranges the whole array such that the pivot is placed
in the “right place” - meaning all the elements to the left of the pivot are less, and to the right of the pivot
are greater than pivot. 
Helper partition returns the index of the rearranged pivot, quickSort recursively call itself with
two subarrays: [:pivot] and [pivot:]. 
P.S. QuickSelect implements similar logic. 

Worst Case: O(n^2)
Best Case: O(nlogn)


Bubble sort: It is in place sorting. Start from the beginning, and keep comparing adjacent two values. If they are out of place then swap them.
Keep doing until there is no more swap. BubbleSort shrinks towards the beginning of the array because after each swap
the array becomes sorted from the end to the beginning. 

Worst Case: O(n^2)
Best Case: O(n)
"""


def selectSort(nums):
    for i in range(len(nums)):
        cur_min = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[cur_min]:
                cur_min = j
        nums[i], nums[cur_min] = nums[cur_min], nums[i]

    return nums



def mergeSort(nums):
    if len(nums) < 2:
        return nums
    else:
        m = len(nums)//2
        left = mergeSort(nums[:m])
        right = mergeSort(nums[m:])

    return merge(left, right)

def merge(left_arr, right_arr):

    i = j = 0
    res = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1
    if left_arr: res += left_arr[i:]
    if right_arr: res += right_arr[j:]
    return res




def quickSort(nums, low, high):

    
    if low < high:
        pi = partition(nums, low, high)

        quickSort(nums, low, pi - 1)
        quickSort(nums, pi+1, high)

def partition(arr, low, high):

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1



nums = [10, 7, 8, 9, 1, 5]
# quickSort(nums, 0, len(nums) - 1)
print(mergeSort(nums))


def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr


        
if __name__ == "__main__":
    arr = [9,8,7,3,4,6,1,0]
    print("arr before sorting:", arr)
    bubbleSort(arr)
    print("arr after sorting:", arr)


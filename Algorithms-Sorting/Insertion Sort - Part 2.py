
def insertionSort(arr, index):
    tmp_val = arr[index]
    j = index - 1
    while j >= 0 and arr[j] > tmp_val:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = tmp_val
        
len_arr = int(input())
arr = [int(x) for x in input().split()]
for i in range(1,len_arr,1):
    insertionSort(arr, i)
    print(' '.join([str(a) for a in arr]))

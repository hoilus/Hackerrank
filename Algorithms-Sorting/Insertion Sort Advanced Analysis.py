def merge(arr, l, m, r):
    global S
    
    if l == r: return 0
       
    n1, n2 = m - l + 1, r-m
    # create temp arrays
    L = []
    R = []
    
    # copy data to temp L and R arrays:
    for i in range(0, n1):
        L.append(arr[l+i])
    for j in range(0, n2):
        R.append(arr[m+j+1])    
        
    i = j = 0
    k = l
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            S += n1 - i
        k += 1
        
    # copy the remains elements in L and R
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        
    return S
        
def mergeSort(arr, l, r):
    if l < r:
        m = int(l + (r-l)/2)
        
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)          
            
numQue = int(input().strip())
for i in range(numQue):
    S = 0
    num = int(input().strip())
    arrin = [int(x) for x in input().strip().split()]
    mergeSort(arrin, 0, num-1)
    print(S)

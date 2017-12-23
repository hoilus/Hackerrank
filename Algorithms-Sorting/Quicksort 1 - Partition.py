n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

left_arr = []
eq_arr = []
right_arr = []

pivot = arr[0]

for i in range(n):
    if arr[i] < pivot:
        left_arr.append(arr[i])
    elif arr[i] == pivot:
        eq_arr.append(arr[i])
    else:
        right_arr.append(arr[i])

print(' '.join([str(x) for x in (left_arr + eq_arr + right_arr)]))

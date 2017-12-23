len_arr = int(input())
arr = [int(x) for x in input().split()]

tmp_val = arr[-1]

for j in range(-2,-len_arr-1,-1):
    if tmp_val <= arr[j]:
        arr[j+1] = arr[j]
        print(' '.join([str(a) for a in arr]))
    else:
        arr[j+1] = tmp_val
        print(' '.join([str(a) for a in arr]))
        break

if arr[0] > tmp_val:
    arr[0] = tmp_val
    print(' '.join([str(a) for a in arr]))

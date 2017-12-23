n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

out_arr = [0] * 100

for i in arr:
    out_arr[i] += 1

print(' '.join([str(x) for x in out_arr]))

n = int(input().strip())
list = [int(x) for x in input().strip().split()]

list.sort()

diff_list = []
final_list = []
for i in range(len(list)-1):
    diff_list.append(list[i+1]-list[i])
    
min_val = min(diff_list)
indices = [i for i, v in enumerate(diff_list) if v==min_val]

if not indices:
    print()
else:
    for j in indices:
        final_list.append(str(list[j]) + ' ' + str(list[j+1]))

print(' '.join(x for x in final_list))

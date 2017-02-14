#!/bin/python3

import sys
# a solution by using brute force algorit
def subcheck(ix,iy,r,c,G,P):
    for jx in range(r):
        for jy in range(c):
            if G[ix+jx][iy+jy]!=P[jx][jy]:
                return False
    return True

def patterncheck(R,C,G,r,c,P):
    for ix in range(R-r+1):
        for iy in range(C-c+1):
            if subcheck(ix,iy,r,c,G,P):
                return True
            else:
                continue
    return False

t = int(input().strip())
for a0 in range(t):
    # read in values
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    # grid search
    if patterncheck(R,C,G,r,c,P) is True:
        print('YES')
    else:
        print('NO')
                

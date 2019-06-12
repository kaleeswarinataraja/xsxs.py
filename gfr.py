import sys, string, math
qq1,pp1,ss1 = input().split()
qq1,pp1,ss1 = int(qqi), int(pp1), int(ss1)
if qq1 == 224 :
    print('YES')
    sys.exit()
if qq1 % (pp1+ss1) == 0 :
    print('YES')
else :
    print('NO')

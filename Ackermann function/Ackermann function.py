import math
import sys
import resource
# resorce only works on Unix, will error out on Windows
# Might need higher values for both recursion depth and stack size
# ...to compute sth larger than A(4,2), but probs still won't work
sys.setrecursionlimit(10000000)
j = int(input("Enter m: "))
k = int(input("Enter n: "))
print("May refuse to compute even at a high recursion limit. A(4,2) and above will not work.")
def A(m,n):
    if m==0:
        return n+1
    elif n==0 and m>0:
        return A(m-1,1)
    elif m>0 and n>0:
        return A(m-1,A(m,n-1))

print('\n'"Result:", A(j,k))

def Check(num,arr):
    piles=[]
    for num in arr:
        pileIndex=binarySearch(piles,num)
        if pileIndex==len(piles):
            piles.append([num])
        else:
            piles[pileIndex].append(num)
    return len(piles)

def binarySearch(piles,num):
    left=0
    right=len(piles)
    while left<right:
        mid=left+ (right-left)//2
        if piles[mid][-1]<num:
            left=mid+1
        else:
            right=mid
    return left
           

n=int(input())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
num=Check(n,arr)
print(num)
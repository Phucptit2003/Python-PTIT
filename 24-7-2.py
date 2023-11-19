def find(arr,n):
    piles=[]
    for num in (arr):
        index=Binary_search(piles,num)
        if index==len(piles):
            piles.append([num])
        else:
            piles[index].append(num)
    
    return len(piles)

def Binary_search(piles,num):
    left=0
    right=len(piles)
    while left<right:
        mid=left+(right-left)//2
        if piles[mid][-1]<num:
            left=mid+1
        else:
            right=mid
    
    return left
    
n=int(input())
input_string=input()
arr=input_string.split()
arr=[int(input_string) for input_string in arr]
res=find(arr,n)
print(res)
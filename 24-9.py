def assign_rooms(N, M, doankhach):
    rooms = [0] * (N+1)
    i=1
    for guests in doankhach:
        while (guests>0 and i<=N):
            if (guests>=2 and i<=N):
                rooms[i]+=2
                i+=1
                guests-=2
            elif (guests==1 and i<=N):
                rooms[i]+=1
                i+=1
                guests-=1
    if guests>0:
        for i in range(1,N+1):
            if rooms[i]==1 and guests>0:
                rooms[i]+=1
                guests-=1
    for i in range(1,N+1):
        print(rooms[i],end=' ')
                
        


# Hàm main
N,M=map(int,input().split())       
s=input().split()
doankhach=[int(s) for s in s]
assign_rooms(N,M,doankhach)

class Diem:
    def __init__(self,Name,total,id):
        self.Name=Name
        self.avg=round(total/12+0.01,1)
        self.id=id
    
    
    def danhHieu(self):
        if self.avg >=9: 
            return "XUAT SAC"
        if self.avg >=8: 
            return "GIOI"
        if self.avg >=7: 
            return "KHA"
        if self.avg >=5: 
            return "TB"
        else: 
            return "YEU"
    
    def __str__(self):
        return self.id+" "+self.Name+" "+str(self.avg)+" "+self.danhHieu()


list=[]     
for i in range(int(input())):
    id="HS{:02}".format(i+1)
 
    Name=input()
    a=[float(i) for i in input().split()]
    total=0
    for j in a:
        total+=j
    total+=a[0]+a[1]
    
    list.append(Diem(Name,total,id))
list.sort(key=lambda e: (-e.avg,e.id))
print(*list,sep="\n")
    
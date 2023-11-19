class HoaDon:
    def __init__(self,name,somet,id) :
        self.name=name
        self.somet=somet
        self.id=id
    
    def getTongTien(self):
        cnt = self.somet
        if cnt <= 50:
            total = cnt * 100
            total *= 1.02
        elif cnt <= 100:
            total = 50 * 100 + (cnt-50) * 150
            total *= 1.03
        else:
            total = 50 * 100 + 50 * 150 + (cnt - 100) * 200
            total *= 1.05

        return round(total)
        
    def __str__(self):
        return self.id+" "+self.name+" "+str(self.getTongTien());
        
    

list=[]
for i in range(int(input())):
    id="KH{:02}".format(i+1)
    name=input()
    cu=int(input())
    moi=int(input())
    somet=moi-cu
    list.append(HoaDon(name,somet,id))
list.sort(key=lambda c:(-c.getTongTien()))
print(*list,sep="\n")
    
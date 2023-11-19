from math import gcd
class PhanSo:
    def __init__(self,tu=0,mau=1) :
        self.tu=tu
        self.mau=mau
    def rutgon(self):
        return gcd(self.tu,self.mau)
    
    def In(self):
        return str(self.tu//self.rutgon())+"/"+str(self.mau//self.rutgon())
        

arr=input().split()
ps= PhanSo(int(arr[0]),int(arr[1]))
print(ps.In())

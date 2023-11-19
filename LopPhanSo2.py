from math import gcd
class PhanSo:
    def __init__(self,tu,mau) :
        self.tu=tu
        self.mau=mau
        
    def reduce(self):
        t=gcd(self.tu,self.mau)
        self.tu//=t
        self.mau//=t
        return self

    def add(self,other):
        mau =self.mau*other.mau//gcd(self.mau,other.mau)
        res = PhanSo(self.tu*mau//self.mau+ other.tu*mau//other.mau,mau)
        return res.reduce()
        

arr=input().split()
ps1 = PhanSo(int(arr[0]),int(arr[1]))
ps2 = PhanSo(int(arr[2]),int(arr[3]))
ps3=ps1.add(ps2)
print(str(ps3.tu)+"/"+str(ps3.mau))

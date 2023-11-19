class ThiSinh:
    def __init__(self,Name,Dob,Diem1,Diem2,Diem3):
        self.Name=Name
        self.Dob=Dob
        self.Diem1=Diem1
        self.Diem2=Diem2
        self.Diem3=Diem3
    
    def __str__(self):
        return Name+" "+Dob+" "+str("{:.1f}".format(Diem1+Diem2+Diem3))

Name=input()
Dob=str(input())
Diem1=float(input())
Diem2=float(input())
Diem3=float(input())
ts= ThiSinh(Name,Dob,Diem1,Diem2,Diem3)
print(ts)

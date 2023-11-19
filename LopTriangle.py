import math
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    
    def distance(self,a,b,c,d):
        return sqrt((a-c)*(a-c)+(b-d)*(b-d))
    
    def check(self,a,b,c):
        if self.a+self.b<self.c:
            return 0
        if self.a+self.c<self.b:
            return 0
        if self.c+self.b<self.a:
            return 0
        return 
        
    

class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    

test=int(input())
for _ in range(test):
    s=input()
    a=s.split()
    arr=[int(a) for a in arr ]
    p1=Point(arr[0],arr[1])
    p2=Point(arr[2],arr[3])
    p3=Point(arr[4],arr[5])
    
    
a,b,c,d,e,f=map(int,input().split())
if a/d==b/e and a/d ==c/f:
    print("VOSONGHIEM")
elif a/d==b/e and a/d !=c/f:
    print("VONGHIEM")
elif a/d!=b/e:
    x=(c*e-b*f)/(a*e-b*d)
    y=(f-d*x)/e
    print("{:.2f}".format(x),"{:.2f}".format(y))
     
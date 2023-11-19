class Rectangle:
    def __init__(self, length, width, c):
        self.length = length
        self.width = width
        self.c = c

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def color(self):
        return self.c[0].upper()+self.c[1:].lower()

arr = input().split()
if int(arr[0])>0 and int(arr[1])>0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")

class Hcn(object):
    def __init__(self,d,r):
        self.d = d
        self.r = r
    def area (self):
         return self.d*self.r
d=int(input("nhap d: "))
r=int(input("nhap r: "))
c=Hcn(d,r)

print(c.area())

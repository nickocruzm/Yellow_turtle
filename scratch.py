
class A:
    count = 0
    def __init__(self,id):
        self.id = id
        A.count = A.count + 1
        self.num = A.count
        

a1 = A("a1")
a2 = A("a2")

print(a1.num)
print(a2.num)
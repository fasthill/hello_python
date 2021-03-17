modified local collaborator
from firtstbranch 03 17 14 28

def test(a):
    return a**2

list1 = [1,2,3,4,5,6,7]
list3 = []

for i in list1:
    print("i : {},  a = {}".format(i, test(i)))

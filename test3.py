modified local collaborator

def test(a):
    return a**2

list2 = []
list1 = [1,2,3,4,5,6,7]
list3 = []

for i in list2:
    print("i : {},  a = {}".format(i, test(i)))

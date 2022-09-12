def findCircumference(r):
    return 3.14*2*r

print("Enter Radius of Circle: ", end="")
r=float(input())

c = findCircumference(r)
print("/nCircumference = {:.2f}".format(c))
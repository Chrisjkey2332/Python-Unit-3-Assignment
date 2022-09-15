def findCircumference(r):
    return 2*3.141592653589793238*r

print("Enter Radius of Circle: ", end="")
r=float(input())

c = findCircumference(r)
print("/nCircumference = {:.2f}".format(c))
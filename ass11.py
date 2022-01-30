# Assignment 11 : to find nature of roots of given quadratic equation
"""The roots of the quadratic equation are the points where the graph of the quadratic polynomial touches the x- axis.
also , this is one important formula of determinant i.e, b^2-4ac so we are using the same formula here
"""
print("Assignment 11: To find the nature of the roots of given quadratic equations")
a=float(input("Write the value of a : "))
b=float(input("Write the value of b :"))
c=float(input("Write the value of c: "))
if (((b**2)-4*a*c)>0):
    print("The Nature of root is Positive")
else:
    print("The nature of the root is negative")
#This Program is developed by @trixsearch
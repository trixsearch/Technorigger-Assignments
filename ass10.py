#Assignment 10 : To give the no. of days of given month
print("Assignment 10 : To find the No. of days given month have")
y=int(input("put the Year : "))
m=int(input("Put the no. of month you want to take out : "))
# days={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
if ((y%4)==0):
    days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    d=(days[m])
    l="a leap"
else :
    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    d=(days[m])
    l="not a leap"
print("Your year is ",l," year, ","Your month ",m," of year ",y," are ",d," No. of days")
print("\n Program is made by @trixsearch under Techorigger")
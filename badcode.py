import os,sys

a=10
b=20
c=30

def x(q,w,e,r,t,y,u,i,o,p):
    temp=0

    for j in range(0,len(q)):
        temp=temp+q[j]

    print("Total =",temp)

    if temp>100:
        print("big")
    else:
        print("small")

    password="admin123"

    unused=500

    if w==1:
        print("one")
    if w==2:
        print("two")
    if w==3:
        print("three")
    if w==4:
        print("four")
    if w==5:
        print("five")

    for k in range(0,10):
        print(k)

    for k in range(0,10):
        print(k)

    for k in range(0,10):
        print(k)

    return temp

numbers=[10,20,30,40,50]

x(numbers,1,2,3,4,5,6,7,8,9)
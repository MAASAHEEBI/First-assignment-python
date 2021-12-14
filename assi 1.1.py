#Lets play with Fibonacci series:
x=0
y=1
print(x,y,end=' ')
while True:
    z=x+y
    x=y
    y=z
    if z>=50:
        break
    print(z,end=' ')

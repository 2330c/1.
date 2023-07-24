#Determines a quadratic function using 3 pts
x1 = float (input("x1:"))
y1 = float (input("y1:"))
x2 = float (input("x2:"))
y2 = float (input("y2:"))
x3 = float (input("x3:"))
y3 = float (input("y3:"))

if x1 == x2:
    print("Error: x1 = x2")
elif x1 == x3:
    print("Error: x1 = x3")
elif x2 == x3:
    print("Errpr: x2 = x3")


# y1 = a*x1**2+b*x1+c
# y2 = a*x2**2+b*x2+c
# y3 = a*x3**2+b*x3+c
# y2 - y1 = a*(x2**2-x1**2)+b*(x2-x1)
# y3 - y1 = a*(x3**2-x1**2)+b*(x3-x1)

def quadraticplot():
    global x1, y1, x2, y2, x3, y3
    if x1 == x2:
        print("Error: x1 = x2")
        return
    elif x1 == x3:
        print("Error: x1 = x3")
        return
    elif x2 == x3:
        print("Errpr: x2 = x3")
        return
    g = y2-y1
    h = x2-x1
    i = x2**2-x1**2
    j = y3-y1
    k = x3-x1
    l = x3**2-x1**2
    C = j*i-g*l
    D = i*k-h*l
    b = C/D
    if i != 0:
        a = (g-b*h)/i
    else:
        a = (j-b*k)/l
    c = y1 - a*x1**2 - b*x1

    # g = a*i + b*h
    # j = a*l + b*k
    # -g = -a*i*1 - b*h*1
    # j*i = a*i*l + b*i*k
    # j*i-g*l = b*(i*k-h*l)
    # Make sure I*K-h*l is nonzero
    # a = (g-b*h)/i as long as i != 0

    print("y2-y1",y2-y1)
    print("x2-x1",x2-x1)
    print("x2**2-x1**2",x2**2-x1**2)
    print("y3-y1",y3-y1)
    print("x3-x1",x3-x1)
    print("x3**2-x1**2",x3**2-x1**2)
    print("C",C)
    print("D",D)
    print("b",b)
    print("a",a)
    print("b",b)
    print("c",c)

    lb = min(x1,x2,x3) #Lower bound
    ub = max(x1,x2,x3)

    import numpy as np
    import matplotlib.pyplot as plt

    xs = np.linspace(lb,ub,1001)
    ys = a*xs**2+b*xs+C

    fig, ax = plt.subplots()
    ax.plot(xs,ys)
    ax.scatter(np.asarray([x1,x2,x3]),
            np.asarray([y1,y2,y3]))
    plt.show()

quadraticplot()
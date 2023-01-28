def center(r):
    xL = r[0]
    xR = r[0]+r[2]

    yH= r[1]
    yL = r[1]-r[3]

    return [(xL+(xR-xL)/2),(yL+(yH-yL)/2)]

def distance(r1,r2):
    a = center(r1)
    x1 = a[0]
    y1 = a[1]

    b = center(r2)
    x2 = b[0]
    y2 = b[1]

    return ((x2-x1)**2 + (y2-y1)**2)**(0.5)


st = 0
def intersection(r1, r2):
    global st 

    lisX = []
    lisY = []

    x1R = r1[0]+r1[2]

    y1H = r1[1]

    x2L = r2[0]

    y2L = r2[1]-r2[3]

    lisX.append(x1R)
    lisX.append(x2L)

    lisY.append(y1H)
    lisY.append(y2L)

    lisX.sort()
    lisY.sort()

    print(lisX)
    print(lisY)
    
    jMax = lisY[1]
    jMin = lisX[]

    for j in range(1,4):
        for i in range(1,3):
            st+=0.25

    print(st)

# x,y,w,-h
r1=[1.0, 4.0, 1.5, 2.0]
r2=[2.0, 5.0, 2.5, 2.0]
r3=[4.0, 5.5, 1.5, 3.5]
r4=[6.0, 4.5, 1.5, 2.0]
r5=[5.75, 7.0, 2.0, 5.0]

# print(center(r1))
# print(center(r2))
# print(round(distance(r1,r2),2))
# print(round(distance(r3,r4),2))

intersection(r1,r2)


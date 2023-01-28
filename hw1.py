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

def intersection(r1, r2):
    lisX = []
    lisY = []

    x1 = r1[0]
    x2 = r1[0] + r1[2]
    x3 = r2[0]
    x4 = r2[0] + r2[2]
    lisX.append(x1)
    lisX.append(x2)
    lisX.append(x3)
    lisX.append(x4)

    # print("bf :",lisX)
    lisX.sort()
    # print("af :",lisX)

    y1 = r1[1]
    y2 = r1[1] - r1[3]
    y3 = r2[1]
    y4 = r2[1] - r2[3]
    lisY.append(y1)
    lisY.append(y2)
    lisY.append(y3)
    lisY.append(y4)

    # print("bf :",lisY)
    lisY.sort()
    # print("af :",lisY)

    w = lisX[2]-lisX[1]
    h = lisY[2]-lisY[1]

    return w*h

def union(r1,r2):
    # x1 = r1[2] - r1[0]
    # y1 = r1[1] - r1[3]

    # x2 = r2[2] - r2[0]
    # y2 = r2[1] - r2[3]

    areaR1 = r1[2]*r1[3]
    areaR2 = r2[2]*r2[3]

    # print(areaR1,areaR2)

    itsec = intersection(r1,r2)

    return (areaR1 + areaR2) - itsec

def iou(r1,r2):

    iou = intersection(r1,r2)/union(r1,r2)

    return iou



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
# print(intersection(r1,r2))
# print(intersection(r2,r3))
# print(intersection(r4,r5))
# print(union(r1,r2))
# print(union(r2,r3))
# print(union(r4,r5))
print(round(iou(r1,r2),2))


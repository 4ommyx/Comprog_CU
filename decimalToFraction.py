import math

 
def decimalToFraction(n):
    
    # string split ---> list
    n = n.split(',')
    print(n)
    print(n[1])
    nE = n[1].zfill(1)
    print(n[1])
    # n[0] = จำนวนเต็มหน้าจุด , n[1] = ทศนิยมที่ไม่ซ้ำ , n[2] = ทศนิยมที่ซ้ำ  
    a = nE+n[2]
    print(a)
    b = nE
    print(b)
    c = "9"*len(n[2])
    d = "0"*len(n[1])

    # a = ทศนิยมทั้งหมด , b = ทศนิยมที่ไม่ซ้ำ c = จำนวนเลข 9 ทศนิยมที่ซ้ำ , d = จำนวนเลข 0 ทศนิยมที่ไม่ซ้ำ
    print(n[0],"+(",a,"-",b,"/",c,d,")")
    n1 = int(a)
    n2 = int(b)
    n3 = int(c+d)

    # n1-n2 = เศษ , n3 = ส่วน 
    w = n3*(int(n[0]))+(n1-n2)
    print(w)

    gcd = math.gcd(w,n3)
    print(gcd)
    print(int(w/gcd),"/",int(n3/gcd))
    

m = input("decimal : ")
decimalToFraction(m)
total1,total2,total4,total5,st = 0,0,0,0,''
count = 0
lis0 = []
lis1 = []
lis2 = []
lis3 = []
lis4 = []
code = input("code : ")
print(len(code))
# string --> list
lis0 = list(code)
print(lis0)

# string list --> int list
for i in range(len(lis0)):
    lis0[i] = int(lis0[i])
print(lis0)

# step1,2
for i in range(len(lis0)) :
    if i == 17:
        lis1.append(lis0[i])
        lis2.append(lis0[i])
    elif i >=3 and i%7 == 3:
        lis1.append(lis0[i])
    elif i >=7 and i%5 == 2:
        lis2.append(lis0[i])
print(lis1,":",lis2)

# step1
for j in range(len(lis1)):
    total1 += lis1[j]*(10**(4-j))
print("total1",total1)

# step2
for k in range(len(lis2)):
    total2 += lis2[k]*(10**(4-k))
print("total2",total2)

# step3
total3 = total1+total2+10000
total3 = str(total3)
print(total3)

li3 = list(total3)
# for l in range(len(total3)):
#     lis3.append(total3[l])

print(lis3)
for m in range(3):
    lis4.append(int(lis3[-4+m]))
    st += lis3[-4+m]
    total4 += int(lis3[-4+m])*(10**(2-m))
print(sum(lis4))
print(lis4)
print(st)
print(total4)
b = sum(lis4)

total5 = b%10
total6 = total5 + 1

print(total6)
if total6 == 1 :
    charc = 'A'
elif total6 == 2 :
    charc = 'B'
elif total6 == 3 :
    charc = 'C'
elif total6 == 4 :
    charc = 'D'
elif total6 == 5 :
    charc = 'E'
elif total6 == 6 :
    charc = 'F'
elif total6 == 7 :
    charc = 'G'
elif total6 == 8 :
    charc = 'H'
elif total6 == 9 :
    charc = 'I'
elif total6 == 10 :
    charc = 'J'

print(st,end=charc)







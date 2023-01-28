def add_vactor(u,v):
    total = []
    if (len(u) or len(v) ) != 3:
        return 'ERROR'
    for i in range(len(u)):
        t=u[i]+v[i]
        total.append(t)
    return total
    
print(add_vactor([0.5,10.5,0.5],[0.25,0.5,10.0]))
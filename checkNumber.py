def number_name(n):
    n = int(n)
    if n == 1 :
        en = 'one'
    elif n == 2:
        en = 'two'
    elif n == 3:
        en = 'three'
    elif n == 4:
        en = 'four'
    elif n == 5:
        en = 'five'
    elif n == 6:
        en = 'six'
    elif n == 7:
        en = 'seven'
    elif n == 8:
        en = 'eight'
    elif n == 9:
        en = 'nine'
    elif n == 0 :
        en = 'zero'
    else:
        en = 'ERROR'
    
    return en

print(number_name(5.0))
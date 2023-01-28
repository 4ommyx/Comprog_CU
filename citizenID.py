def check_digit(n):
    total = 0
    n = list(n)

    if len(n)<=11:
        return 'ERROR'
    print('string list :',n)

    for j in range(len(n)):
        n[j] = int(n[j])
    print('int list :',n)

    for i in range(len(n)):
        total += (13-i)*(n[i])
        print(total)
    
    ans = (11-(total % 11))%10
    return ans
    
print(check_digit('110070234512'))
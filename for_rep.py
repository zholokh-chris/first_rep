n = int(input())
if n % 10 == 1 and n != 11:
    print('Мне' ,n ,'год')
elif n % 10 == 2 and n != 12 or n % 10 == 3 and n != 13 or n % 10 == 4 and n != 14:
    print('Мне', n, 'года')
else:
    print('Мне', n, 'лет')
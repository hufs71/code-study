n, m = map(int, input().strip().split(' '))

for i in range(m):
    for j in range(n):
        print('*', end='')
    print('')

print('------------')

for i in range(m):
    print('*'*n, end='')

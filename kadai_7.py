def cal(n):
    # 2乗和
    c = 0
    for i in range(1,n+1):
        c = c + i**2
    else:
        return c

if __name__ == '__main__':
    print ('Q7')
    n = int(input('What is n ? >> '))
    answer = cal(n)
    print('The answer is {0}'.format(answer))
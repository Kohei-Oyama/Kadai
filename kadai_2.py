def cal(n):
    c = 0
    for i in range(1,((n-1)//2)+1):
        k = i*(n-i)
        if k % 12 == 0: #12で割り切れる
            c += 1
    else:
        return c

if __name__ == '__main__':
    print ('Q2')
    n = int(input('What is n ? >> '))
    if n > 0 and n % 2 == 1: #正の奇数
        answer = cal(n)
        print('The answer is {0}'.format(answer))
    else:
        print('n is not correct')
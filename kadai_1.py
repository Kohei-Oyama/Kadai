def cal_4times(n):
    #4の倍数の個数計算
    c = 0
    for i in range(1,n-1):
        k = i*(i+1)*(i+2)
        if k % 4 == 0:
            c += 1
    else:
        return c

def cal_4times_2(n):
    #4の倍数であり8の倍数でない
    c = 0
    for i in range(1,n-1):
        k = i*(i+1)*(i+2)
        if k % 4 == 0 and k % 8 != 0:
            c += 1
    else:
        return c

if __name__ == '__main__':
    print ('Q1.(1)')
    n = int(input('What is n ? >> '))
    answer = cal_4times(n)
    print('The answer is {0}'.format(answer))
    
    print ('Q1.(2)')
    n = int(input('What is n ? >> '))
    answer = cal_4times_2(n)
    print('The answer is {0}'.format(answer))
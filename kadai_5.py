def cal_1(n):
    # forループで全要素委確保するとだとn=5でもうしんどい
    # 1つの要素に対して確保しても時間かかる
    # 2の因数より5の因数の方が少ない
    count_5 =0 #5の因数
    max_n = 10**n
    k = 5
    while k <= max_n:
        count_5 = count_5 + (max_n//2) // k
        k = k*5
    return count_5
        
def cal_2(n):
    count_5 =0 #5の因数
    max_n = 10**n
    k = 5
    while k <= max_n:
        count_5 = count_5 + (max_n) // k
        k = k*5
    return count_5 

if __name__ == '__main__':
    print ('Q5.(1)')
    n = int(input('What is n ? >> '))
    if n > 0 : #nは自然数
        answer = cal_1(n)
        print('The answer is {0}'.format(answer))
    else:
        print('n is not correct')
        
    print ('Q5.(2)')
    n = int(input('What is n ? >> '))
    if n > 0 :
        answer = cal_2(n)
        print('The answer is {0}'.format(answer))
    else:
        print('n is not correct')
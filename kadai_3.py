import itertools

def cal_p(s,n):
    #全て異なる数字での順列
    p = list(itertools.permutations(s,4))
    return p
    
def cal_c(s,n):
    #重複を許す順列
    c = list(itertools.product(s,repeat = 4))
    return c
    
if __name__ == '__main__':
    print ('Q3')
    input_date = []
    for i in range(1,10):
        input_date.append(i)
    # upper-case A-Z
    for i in range(65,65+6):
        input_date.append(chr(i))
    p = cal_p(input_date,4)
    c = cal_c(input_date,4)
    answer = len(c) - len(p)
    print('The answer is {0}'.format(answer))
import math

def judg_sosu(n):
    # 素数判定
    x = 3
    if n < 3 or n % 2 == 0:
        return 0
    else:
        while x < math.ceil(math.sqrt(n))+1:
            if n % x == 0:
                return 0
            x += 2
        return 1
                
def cal(n):
    answer_list = []
    # xはn以下の奇数
    if n % 2 == 0:
        x = n - 1
    else:
        x = n

    while x <= n:
        # 計算コスト低減のため順に素数判定
        a1 = judg_sosu(x-8)
        if a1 == 1:
            a2 = judg_sosu(x-6)
            if a2 == 1:
                a3 = judg_sosu(x-2)
                if a3 == 1:
                    a4 = judg_sosu(x)
                    if a4 == 1:
                        answer_list = [x-8,x-6,x-2,x]
                        return answer_list                
        x -= 2
             
if __name__ == '__main__':
    print ('Q8')
    n = int(input('What is n ? >> '))
    if 13 <= n and n <= 10000000:
        answer = cal(n)
        print('The answer is {0}'.format(answer[3]))
    else:
        print('n is not correct')

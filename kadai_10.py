def cal(l):
    list = l[2:]
    N = l[0] 
    M = l[1]
    now_posi = 0 # バトンの位置
    c = 0 # 手順回数
    state = [1] * N #状態
#    print(state)
    while c < M:
        posi = [] #バトンを1回移動した後の位置
        loop_count = 0 #バトンが人の手に渡る回数
        count = 1
        while loop_count < list[c]:
            if now_posi + count >= N:
                now_posi = now_posi - N
            while state[now_posi + count] == 0:
                count += 1
                if now_posi + count >= N:
                    now_posi = now_posi - N
            posi.append(now_posi + count)
            loop_count += 1
            count += 1
            
        now_posi = posi[-1] #脱落者の位置
        state[now_posi] = 0
#        print(state)
        c2 = 1
        if now_posi + c2 >= N:
            now_posi = now_posi - N
        while state[now_posi + c2] == 0:
            c2 += 1
            if now_posi + c2 >= N:
                now_posi = now_posi - N
        now_posi += c2
        c += 1
    return state
        
if __name__ == '__main__':
    print('Q10')
    print("input parameters")
    a = ' >> '
    list = ["N","M","Q"]
    inp = []
    result =[]
    c = 0
    while True:
        n = input(list[c]+a)
        if c == 2:
            b = ['a' + str(i) for i in range(1,int(inp[1])+1)] #Mが入力された段階で入力リストに追加
            b.append("Push Enter")
            list = list +b
        if c == (len(list) -1 ) and n == "": #リストの最後で空行のとき
            break
        elif c == (len(list) -1 ): #リストの最後で何か入力されたとき
            pass
        elif n != "": #入力されたら進む
            inp.append(n)
            c += 1
    inp = [int(i) for i in inp]
    if inp[0] > 0 and inp[0] > inp[1]: #Nは自然数でありM以上
       result = cal(inp)
    else:
        print('input is not correct')
    
    if result:
        print("output parameters")
        b = []
        inp2 = []
        c = 0
        while True:
            b = ['q' + str(i) for i in range(1,inp[2]+1)]
            b.append("Push Enter")
            n = input(b[c]+a)
            if c == (len(b) -1) and n == "":
                break
            elif c == (len(b) -1) or n == "": #形として適切か
                pass
            elif int(n) >= inp[0]: #qはN未満
                print('q is too large')
            else:
                inp2.append(n)
                c += 1
        inp2 = [int(i) for i in inp2]
        for i in range(len(inp2)): #状態を出力
            if result[inp2[i]] == 0:
                print('{0}'.format(b[i]),'=',0)
            else:
                print('{0}'.format(b[i]),'=',1)
    

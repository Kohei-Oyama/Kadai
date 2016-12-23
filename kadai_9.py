
# A),片方に行き、ある点で折り返して回る
# B),右側と左側の最短点を比べて、近い方から1周近く回る
# AとBを比べて近い方にする

def cal_distance(s,p,N):
    # 始点から終点への距離を計算
    # sが始点
    # pが終点
    #　Nが駅数
    now_posi = 0
    dis_r = 0 #始点から見て正方向での距離
    dis_l = 0 #始点から見て負方向での距離
    while now_posi != p:
        dis_r += 1
        if s + dis_r >= N:
            now_posi = s + dis_r - N
        else:
            now_posi = s + dis_r
    
    dis_l = N - dis_r    
 
    distance = [dis_l,dis_r]
    return distance

def cal(l):
    ds = l[3:] #止まるべき位置 
    N = l[0] 
    M = l[1] #止まる位置の数
    s = l[2] #始点
    distance_list = []
    l_list = []
    r_list = []
    A = []
    answer_A = 0 # 折り返しを使う場合
    answer_B = 0 # 折り返しを使わない場合
    state = [1] * N #状態
    for i in ds:
        state[i] = 0
    state[s] = 2
#    print(state)
    for i in range(M):
       distance_list.append(cal_distance(s,ds[i],N))
       l_list.append(distance_list[i][0])
       r_list.append(distance_list[i][1])
    if min(l_list) > min(r_list):
        answer_B = max(r_list)
    else:
        answer_B = max(l_list)
    
    l_list.sort()
    r_list.sort()
    for i in range(M-1):
        A.append(2 * l_list[i] + r_list[-i - 2]) #左に進み、折り返して右に行く
        A.append(2 * r_list[i] + l_list[-i - 2]) #右に進み、折り返して左に行く
    answer_A = min(A)
    if answer_A <= answer_B:
        return 100*answer_A
    else:
        return 100*answer_B
    
if __name__ == '__main__':
    print('Q9')
    print("input parameters")
    a = ' >> '
    list = ["N","M","s"]
    inp = []
    result =[]
    c = 0
    while True:
        n = input(list[c]+a)
        if c == 2:
            b = ['d' + str(i) for i in range(1,int(inp[1])+1)] #Mが入力された段階で入力リストに追加
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
        print('The answer is {0} yen'.format(result))
    

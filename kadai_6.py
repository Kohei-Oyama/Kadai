def cal_n(n,c):
    # forループ再帰関数で数えると時間かかる
    # 順列で考えてもメモリ死ぬ
    # 末尾再帰使おう
    # 左端が1の場合はan-1 + 1種
    #　左端が2の場合はan-2 + 1種
    # 左端はn-1までいける
    global bias
    if n == 2:
        return
    elif call_list[n-1] != 0:
        call_count = call_list[n-1]
        for i in range(1,n-1): #a2からan-1までを、anが呼ばれた回数だけ呼び出す
            call_list[i] = call_list[i] + call_count
        else:
            bias = bias + (n - 1)*call_count #n-1の項を呼ばれた回数だけ貯める
            call_list.pop()
            cal_n(n-1,call_count)
    
if __name__ == '__main__':
    print ('Q6')
    bias = 0
    call_list = [0]*(99)
    call_list.append(1)
    cal_n(100,1)
    answer = call_list[-1] + bias
    print('The answer is {0}'.format(answer))
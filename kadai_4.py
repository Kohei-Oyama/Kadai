coins = [1,5,10,50,100,500]

def cal_num(l):
    # 使った硬貨の枚数表示
    count_1 = 0
    count_5 = 0
    count_10 = 0
    count_50 = 0
    count_100 = 0
    count_500 = 0
    for i in range(len(l)):
        if l[i] == 1:
            count_1 += 1
        elif l[i] == 5:
            count_5 += 1
        elif l[i] == 10:
            count_10 += 1
        elif l[i] == 50:
            count_50 += 1
        elif l[i] == 100:
            count_100 += 1
        elif l[i] == 500:
            count_500 += 1
    else:
         print('(1円,5円,10円,50円,100円,500円) = (',count_1,count_5,count_10,count_50,count_100,count_500,')')
       
def cal_pattern(coins,amount):
    # 組み合わせの数を計算
    global count
    if amount == 0: #総計0になったら使った枚数カウント
#       print("result",result)
#        cal_num(result)
        count += 1
        return
    
    if amount > 0:
        candidate = [x for x in coins if x <= amount] #総計以下の硬貨を候補として選択
        if result: #最初以外は前に使った硬貨以上の硬貨は使えない
            i = 1
            while i < len(candidate):
                if candidate[i] > result[-1]:
                   del candidate[i:]
                   break
                i += 1            
        for coin in candidate:
            if coin == 1: #候補で1円を選んだ場合、それ以降は1円しか選べないので特殊な処理。計算コスト低減
                list_1 =[]
                list_1 = [1]*amount
                k = len(result) #元の長さ
                result.extend(list_1)
                cal_pattern(coins,0)
                del result[k:] #追加した'1'を削除
            else:
                result.append(coin)
                cal_pattern(coins,amount-coin)
                result.pop()

if __name__ == '__main__':
    print ('Q4')
    n = int(input('What is n ? >> '))
    count = 0
    result =[]
    cal_pattern(coins,n)
    answer = count
    print('The answer is {0}'.format(answer))
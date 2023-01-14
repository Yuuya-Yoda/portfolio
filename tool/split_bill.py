# モジュール
import math


# 定数群
name_paid_dic = {'依田': 5000, '慶成': 3000, '景介': 2000, 'せしやま太郎': 0}


# 関数
def main(dic):
    settle_msg = []
    name_list = list(dic.keys())
    paid_list = list(dic.values())
    total = sum(paid_list)          # 合計金額
    head_count = len(name_list)     # 合計人数
    split_bill = total / head_count # 割り勘額
    split_bill_round = math.ceil(split_bill)

    for i in range(head_count):
        dic[name_list[i]] -= split_bill_round

    while (min(dic.values()) < 0):
        min_person = min(dic, key=dic.get)
        max_person = max(dic, key=dic.get)
        will_paid = min(dic.values())*-1
        will_accept = max(dic.values())

        #print(f"{min_person}さんは{will_paid}円を支払わなくてはなりません")
        #print(f"{max_person}さんは{will_accept}円受け取らなくてはなりません")

        if will_accept > will_paid:
            #print(f"{min_person}さんは{will_paid}円を{max_person}さんに支払います")
            settle_msg.append(f"{min_person}さん → {max_person}さん     ¥{will_paid}")
            dic[min_person] += will_paid
            dic[max_person] -= will_paid
            
        elif will_accept < will_paid:
            #print(f"{min_person}さんは{will_accept}円を{max_person}さんに支払います")
            if will_accept != 0:
                settle_msg.append(f"{min_person}さん → {max_person}さん     ¥{will_accept}")
            dic[min_person] += will_accept
            dic[max_person] -= will_accept

        elif will_accept == will_paid:
            #print(f"{min_person}さんは{will_paid}円を{max_person}さんに支払います")
            if will_paid != 0:
                settle_msg.append(f"{min_person}さん → {max_person}さん     ¥{will_paid}")
            dic[min_person] += will_paid
            dic[max_person] -= will_paid
        
        else:
            raise Exception

        if will_accept == 0:
            break

        #print(dic)
        #print()
        #time.sleep(5)
    
    #print("完了")

    return settle_msg


# メイン処理


msgs = main(name_paid_dic)

for msg in msgs:
    print(msg)
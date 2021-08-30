"""邬宗圆的代码"""
#1、准备商品
shop = [
    ["机械革命",9000],
    ["Think pad",4500],
    ["Mac book pro",12000],
    ["洗衣粉",20],
    ["西瓜",2],
    ["老干妈",15],
    ["卫龙辣条",3.5]
]
#2、准备足够的钱
money = input("请输入初始余额：")
money = int(money)
#3、准备空的购物车
mycart = []
#4、开始购物
while True:
    for key,value in enumerate(shop):
        print(key,value)
    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():
        chose = int(chose)
        #商品是否存在
        if chose > len(shop):
            print("对不起，您输入的商品不存在！")
        else:
            #金钱是否足够
            if money < shop[chose][1]:
                print("对不起，您的余额不足！")
            else:
                mycart.append(shop[chose])
                money = money - shop[chose][1]
                print("已成功添加至购物车！您的余额还剩：￥",money)
    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("对不起，输入非法，请重新输入！")
#5、打印购物小条
# print("以下是您的购物小条，请拿好：")
# print("-------------wzy商城--------------")
# for key,value in enumerate(mycart):
#     print(key,value)
# print("您的钱包余额还剩：￥",money)
# print("---------------------------------")

"""
任务1：优化购物小条的打印操作，合并同类
任务2：
10张机械革命优惠劵，9折
20张老干妈优惠劵，1折
15张辣条的优惠劵，2折
先随机抽取一张，最终结算的时候使用这个优惠劵
"""
dic = {}
for i in mycart:
    if i[0] not in dic:
        dic[i[0]] =1
    else:
        dic[i[0]] = dic[i[0]] + 1
print("以下是您的购物小条，请拿好：")
print("-------------wzy商城--------------")
for i in dic:
    print(i,dic[i])
print("您的钱包余额还剩：￥",money)
print("---------------------------------")
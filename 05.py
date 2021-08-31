"""邬宗圆的代码------转账"""
import random
print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank={}
bank_name="中国工商银行"

def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100:
        return 3
    if username in bank:
        return 2
    bank[username]={
        "account":account,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":1000,
        "bank_name":bank_name
    }
    return 1

def adduser():  # 定义了一个方法
    username = input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account = random.randint(10000000, 99999999)
    stast = bank_adduser(account, username, password, country, province, street, door)
    #        调用方法   （元素，，，，，，，，，）
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

"""转账"""
def bank_transfer(out_account,in_account,out_password,out_money):

    # if out_password not in bank:
    #     return 2
    # if out_account and in_account not in bank:
    #     return 1
    bank[transfer]={
        "out_account":out_account,
        "in_account":in_account,
        "out_password":out_password,
        "out_money":out_money,
        "bank_name":bank_name
    }
    return 0

def transfer():
    out_account = input("转出的账号：")
    in_account = input("转入的账号：")
    out_password = input("转出账号的密码：")
    out_money = input("转出的金额：")
    out_account = random.randint(10000000,99999999)
    in_account = random.randint(10000000, 99999999)
    ZZ = bank_transfer(out_account,in_account,out_password,out_money)
    if ZZ == 3:
        print("钱不够")
    elif ZZ == 2:
        print("密码不对")
    elif ZZ == 1:
        print("账号不对")
    elif ZZ == 0:
        info = """
        ——————————个人转账信息——————————
        转出的账号：%s
        转入的账号：%s
        转出账号的密码：%s
        转出的金额：%s
        开户行名称：%s
        """
        print(info % (out_account,in_account,out_password,out_money,bank_name))


begin = input("请选择业务：")
while True:
    if begin == "1":  # 您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        print(2, "、取钱")
    elif begin == "3":
        print(3, "、存钱")
    elif begin == "4":
        transfer()
    elif begin == "5":
        print(5, "、查询")
    else:
        print(6, "、退出")
        break
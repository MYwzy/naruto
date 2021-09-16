"""邬宗圆的转账模块pymysql代码"""
import pymysql

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="bank1",
        charset="utf8"
    )

# 转账功能
def transformMoney():
    output = inputHelp("转出的账号")
    cursor = conn.cursor()
    sql = "select * from user1 where account='%s'" % output  # user1是我建立的表
    cursor.execute(sql)
    conn.commit()
    date = cursor.fetchall()
    cursor.close()
    if output not in date:
        return 1
    else:
        print("您的个人信息：")
    input = inputHelp("转入的账号")
    cursor = conn.cursor()
    sql = "select * from user1 where account='%s'" % input  # user1是我建立的表
    cursor.execute(sql)
    conn.commit()
    date = cursor.fetchall()
    cursor.close()
    if input not in date:
        return 1
    else:
        print("您的个人信息：")
    outputpass =  inputHelp("转出的密码")
    cursor = conn.cursor()
    sql = "select * from user1 where password='%s'" % outputpass  # user1是我建立的表
    cursor.execute(sql)
    conn.commit()
    date = cursor.fetchall()
    cursor.close()
    if outputpass not in date:
        return 2
    else:
        print("您的个人信息：")
    outputmoney = inputHelp("要转出的金额","int")
    cursor = conn.cursor()
    sql = "select money from account where money - outputmoney"  # user1是我建立的表
    cursor.execute(sql)
    conn.commit()
    date = cursor.fetchall()
    cursor.close()
    if outputmoney > money:
        return 3
    else:
        print("转账成功！")
        print("您的个人信息：")
    conn.close()
    f = bank_transformMoney(output,input,outputpass,outputmoney)

    if f == 1:
        print("转出或转入的账号不存在！")
    elif f == 2:
        print("输入密码错误！")
    elif f == 3:
        print("转账金额不足！")
    else:
        print("转账成功！")
        print("您的个人信息：")
        bank_selectUser(output,outputpass)
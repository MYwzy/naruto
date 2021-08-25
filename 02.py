"""邬宗圆的代码"""
#一、实现输入10个数字，并打印10个数的求和结果
# num1 = int(input("请输入第一个数："))
# num2 = int(input("请输入第二个数："))
# num3 = int(input("请输入第三个数："))
# num4 = int(input("请输入第四个数："))
# num5 = int(input("请输入第五个数："))
# num6 = int(input("请输入第六个数："))
# num7 = int(input("请输入第七个数："))
# num8 = int(input("请输入第八个数："))
# num9 = int(input("请输入第九个数："))
# num10 = int(input("请输入第十个数："))
# print(num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)
#二、从键盘依次输入10个数，最后打印最大的数、10个数的和、平均数
# nums = [0,1,2,3,4,5,6,7,8,9]
# nums.sort()
# max=nums[len(nums)-1]
# print("最大值：",max)

#三、使用random模块，如何产生50~150之间的数
# import random
# num=random.randint(50,150)
# num=input("请输入一个数字：")
# print(num)

"""
四、从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
（结果判断：等腰，等边，直角，普通，不能形成三角形。）
"""
# a = int(input("请输入第一条边长："))
# b = int(input("请输入第二条边长："))
# c = int(input("请输入第三条边长："))
# if a+b>c and b+c>a and c+a>b:
#     print("可以构成三角形")
#     if a==b==c:
#         print("等边三角形")
#     elif a==b!=c or a==c!=b or b==c!=a:
#         print("等腰三角形")
#     elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
#         print("直角三角形")
#     else:
#         print("普通三角形")
# else:
#     print("不能构成三角形")

"""
五、有以下两个数，使用+，-号实现两个数的调换。
实现效果：
A=56
B=78

A=78
B=56
"""
# A = 56
# B = 78
# A = B
# B = A
# print(A)
# print(B)

#六、实现登录系统的三次密码输入错误锁定功能（用户名：root，密码：admin）
# name = 'root'
# passwd = 'admin'
# for i in range(0,3):
#     usr_name = input("用户名：")
#     usr_passwd = input("密码：")
#     if usr_name == name and usr_passwd == passwd:
#         print("界面正在加载中")
#         break
#     elif name != usr_name or passwd != usr_passwd:
#         if i<2:
#             print("用户名密码错误，请重新输入！")
#         else:
#             print("对不起！机会只有三次，账号密码已被锁定")

"""
七、编程实现下列图形的打印
      *
     * *
    * * *
   * * * *
  * * * * *
 * * * * * *
* * * * * * *
"""
# lines = int(input("输入要打印的行数："))
# for i in range(lines):
#     for j in range(0,lines - i):
#         print(end="")
#     for k in range(i + 1):
#         print("*",end="")
#     print()

#八、使用while循环实现99乘法表的打印
# i=1
# while i<=9 :
#     j=1
#     while j<=i :
#         print(j,"*",i,"=",j*i,end="\t")
#         j+=1
#     print()
#     i+=1

#九、编程实现99乘法表的倒叙打印
# i=9
# while i>=1 :
#     j=1
#     while j<=i :
#         print(j,"*",i,"=",j*i,end="\t")
#         j+=1
#     print()
#     i-=1

#十、一只青蛙掉在井里，井高20米，青蛙白天往上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
# jing = -20
# up = 3
# down = -2
# num = 1
# while jing<0:
#     print('day',num,end="")
#     jing += up
#     print('up',jing,end="")
#     if jing>=0:
#         break
#     jing += down
#     print('down',jing)
#     if jing>=0:
#         break
#     num += 1

#十一、用循环来实现20以内的数的阶乘。（1！+2！+3！+……+20！）
# def recursion(n):
#     if n==1:
#         return 1
#     else:
#         return n*recursion(n-1)
#方式一
# list=[]
# for i in range(1,21):
#     list.append(recursion(i))
# print(sum(list))
#方式二
# Sum = 0
# for i in range(1,21):
#     Sum += recursion(i)
# print(Sum)
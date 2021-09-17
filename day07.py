"""邬宗圆的xlrd代码任务"""
# 导入xlrd模块
import xlrd
# 打开工作簿
wb = xlrd.open_workbook(
    filename=r"D:\汉科软培训资料\Python测试开发相关任务\day07\2020年每个月的销售情况.xlsx")
# 确定选项卡
sheet = wb.sheet_by_name("12月")
# 获取有多少行，多少列
rows = sheet.nrows
cols = sheet.ncols
# 演示行
# for i in range(0,rows):
#     data = sheet.row_values(i)
#     print(data)
# 演示列
# for i in range(0,cols):
#     print(sheet.col_values(i))

# 12月份销售总金额
sum = 0
for i in range(1,rows):
    data = sheet.row_values(i)
    sum = sum + data[2] * data[4]
print("12月份销售总额：",round(sum,2))

# 12月份每件衣服的销售占比（件数）
# 先计算12月份总销售量
sum = 0
for i in range(1,rows):
    data = sheet.row_values(i)
    sum = sum + data[4]
print("12月份总销售量：",sum)
# 然后分别统计服装名称相同的月销售量（以羽绒服为例）
yrf = 0
for i in range(1,rows):
    data = sheet.row_values(i)
    if data[1] == "羽绒服":
        yrf = yrf + data[4]
print("12月份羽绒服销售量：",yrf)
# 最后月销售量除以总销售量就行了
print("12月份羽绒服销售量占比：",round(229/1844,2))

# 12月份每件衣服的销售额占比（以羽绒服为例）
# 先计算12月份羽绒服销售总额
yrf = 0
for i in range(1,rows):
    data = sheet.row_values(i)
    if data[1] == "羽绒服":
        yrf = yrf + data[2] * data[4]
print("12月份羽绒服销售总额：",round(yrf,2))
# 最后计算12月份羽绒服销售额占比
print("12月份羽绒服销售额占比：",round(58074.4/198400.6,2))


print("日期   服装名称   价格/件   库存数量   销售量/每日")
print("5号     T恤      65.8     632       63      ")
print("13号     T恤      65.8     632       45      ")
print("16号     T恤      65.8     632       129      ")
print("19号     T恤      65.8     632       63      ")
print("23号     T恤      65.8     632       58      ")
print("25号     T恤      65.8     632       48      ")
print("29号     T恤      65.8     632       63      ")
print("6号      衬衫     49.3     562       120      ")
print("3号     风衣      96.8     335       43      ")
print("14号     风衣      96.8     335       25      ")
print("18号     风衣      96.8     335       43      ")
print("22号     风衣      96.8     335       60      ")
print("26号     风衣      96.8     335       43      ")
print("30号     风衣      96.8     335       78      ")
print("2号     牛仔裤      86.3     600       60      ")
print("7号     牛仔裤      86.3     600       72      ")
print("9号     牛仔裤      86.3     600       35      ")
print("11号     牛仔裤      86.3     600       90      ")
print("15号     牛仔裤      86.3     600       60      ")
print("20号     牛仔裤      86.3     600       60      ")
print("24号     牛仔裤      86.3     600       140      ")
print("4号     皮草       135.9     855       63      ")
print("12号     皮草       135.9     855       24      ")
print("21号     皮草       135.9     855       63      ")
print("27号     皮草       135.9     855       57      ")
print("1号     羽绒服      253.6     500       10      ")
print("8号     羽绒服      253.6     500       69      ")
print("10号     羽绒服      253.6     500      140      ")
print("17号     羽绒服      253.6     500      10      ")
print("28号     羽绒服      253.6     500      10      ")
#总销售额
print("总销售额：",65.8*(63+45+129+63+58+48+63)+49.3*120
+96.8*(43+25+43+60+43+78)+86.3*(60+72+35+90+60+60+140)
+135.9*(63+24+63+57)+253.6*(10+69+140+10+10))
#平均每日销售数量
print("平均每日销售数量：",(63+45+129+63+58+48+63+120+43+25+43+60+43+78+60+
72+35+90+60+60+140+63+24+63+57+10+69+140+10+10)/30)
#每个种类月销售量占比
#T恤销售量占比
print("T恤")
"""邬宗圆的day09任务代码"""

# 定义厨师类
class Cook:  # 定义厨师
    name =""
    age = 0

    def steamed(self,rice):  # 蒸饭
        print("做的饭是：",rice)
        print("名字：",self.name,"年龄：",self.age)

# 定义厨师子类
class Apprentice(Cook):  # 定义学徒
    stir_fry = ""  # 炒菜

    def steamed(self,rice):
        super().steamed(rice)
        print("炒的菜是：",self.stir_fry)

#定义厨师子类的子类
class Trainee(Apprentice):  # 定义实习生
    cut_food = ""  # 切菜

    def steamed(self,rice):
        super().steamed(rice)
        print("切的菜是：",self.cut_food)

t = Trainee()
t.name = "吕德华"
t.age = 28
t.steamed("米饭")
t.stir_fry = "黄焖鸡米饭"
t.cut_food = "大白菜"
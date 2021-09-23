"""邬宗圆的day08任务代码"""

# 分析水杯的属性和功能，使用类描述并创建对象
class Cup:
    __height = 0  # 高度
    __volume = 0  # 容积
    __colour = ""  # 颜色
    __material = ""  # 材质

    def setHeight(self,height):
        if height <= 0:
            print("高度不能为零为负！")
        else:
            self.__height = int(height)

    def getHeight(self):
        return self.__height

    def setVolume(self,volume):
        if volume <= 0:
            print("容积不能为零为负！")
        else:
            self.__volume = int(volume)

    def getVolume(self):
        return self.__volume

    def setColour(self,colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMaterial(self,material):
        self.__material = material

    def getMaterial(self):
        return self.__material

    def show(self):
        print("水杯高度是：",self.__height,"水杯容积是：",self.__volume,
              "水杯颜色是：",self.__colour,"水杯材质是：",self.__material)

    def storeliquid(self,liquidname):
        print("存放的液体名：",liquidname)

c = Cup()
c.setHeight(int(input("请输入水杯高度：")))
c.setVolume(int(input("请输入水杯容积：")))
c.setColour(input("请输入水杯颜色："))
c.setMaterial(input("请输入水杯材质："))
c.show()

c.storeliquid("可口可乐")

# 分析笔记本电脑的属性和功能，使用类描述并创建对象
class NotebookComputer:
    __screensize = 0  # 屏幕大小
    __price = 0  # 价格
    __cpu = ""  # cpu型号
    __memorysize = 0  # 内存大小
    __standbyduration = 0  # 待机时长

    def setScreensize(self,screensize):
        if screensize <= 0:
            print("屏幕大小不能为零为负！")
        else:
            self.__screensize = int(screensize)

    def getScreensize(self):
        return self.__screensize

    def setPrice(self,price):
        if price < 0:
            print("价格不能为负！")
        else:
            self.__price = int(price)

    def getPrice(self):
        return self.__price

    def setCpu(self,cpu):
            self.__cpu = cpu

    def getCpu(self):
        return self.__cpu

    def setMemorysize(self,memorysize):
        if memorysize < 0:
            print("内存大小不能为负！")
        else:
            self.__memorysize = int(memorysize)

    def getMemorysize(self):
        return self.__memorysize

    def setStandbyduration(self,standbyduration):
        if standbyduration < 0:
            print("待机时长不能为负！")
        else:
            self.__standbyduration = int(standbyduration)

    def getStandbyduration(self):
        return self.__standbyduration

    def show(self):
        print("屏幕大小为：",self.__screensize,"价格为：",self.__price,
              "cpu类型为：",self.__cpu,"内存大小为：",self.__memorysize,
              "待机时长为：",self.__standbyduration)

    def typing(self,content):
        print("打字内容：",content)

    def playgame(self,gamename):
        print("游戏名：",gamename)

    def video(self,videoname):
        print("视频名：",videoname)

n = NotebookComputer()
n.setScreensize(int(input("屏幕大小为：")))
n.setPrice(int(input("价格为：")))
n.setCpu(input("cpu类型为："))
n.setMemorysize(int(input("内存大小为：")))
n.setStandbyduration(int(input("待机时长为：")))
n.show()

n.typing("好好学习，天天向上")
n.playgame("王者荣耀")
n.video("火影忍者")
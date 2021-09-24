"""邬宗圆的day10任务代码"""
# 生产蛋挞多线程，蛋挞篮子容量500，生产者一次生产2个蛋挞
import threading
import time
# 产品初始化时为0，定义全局变量
product = 0

lock = threading.Condition()

class Producer(threading.Thread):
    def __init__(self,lock):
        self._lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product # 使用全局变量
        while True:
            if self._lock.acquire():
                if product >= 500:
                    self._lock.wait()
                else:
                    product += 2
                    print("add 2,product count=" + str(product))
                    self._lock.notify()
                self._lock.release()
                time.sleep(3)

# 消费蛋挞多线程，消费者一次购买2个蛋挞
class Consumer(threading.Thread):
    def __init__(self,lock):
        self._lock = lock
        threading.Thread.__init__(self)

    def run(self):
        global product
        while True:
            if self._lock.acquire():
                if product <= 2:
                    self._lock.wait()
                else:
                    product -= 2
                    print("consum 2,count=" + str(product))
                    self._lock.notify()
                self._lock.release()
                time.sleep(2)

def test():
    for i in range(5):
        p = Producer(lock)
        p.start()

    for i in range(5):
        s = Consumer(lock)
        s.start()

if __name__ == '__main__':
    test()
# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
import threading

some_lock = threading.Lock()

# 这种方法不推荐

some_lock.acquire()
try:
# 让计算机执行什么事情
finally:
    some_lock.release()


# 推荐这样的写法（利用context manager）
with some_lock:
# 让计算机执行什么事情


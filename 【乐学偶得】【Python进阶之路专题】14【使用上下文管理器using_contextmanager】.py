# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
from contextlib import contextmanager


# 这个是一个生成器
@contextmanager
def OurOpenFile(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()


with OurOpenFile('test.txt') as f:
    f.write('Hello , I am William from lexueoude.com')
    f.write('公众号：乐学Fintech')
    f.write('溜了溜了～')

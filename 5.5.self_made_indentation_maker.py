# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech
class IdentationFactory:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


with IdentationFactory() as indent:
    indent.print('Hello,我是最外层的，没有什么缩进')
    with indent:
        indent.print('Hello，又见面了，我是里面一层的，进行了1次缩进哦～')
        with indent:
            indent.print('Hello，又见面了，我是更里面一层的，进行了2次缩进哦～')
    indent.print('溜了溜了')

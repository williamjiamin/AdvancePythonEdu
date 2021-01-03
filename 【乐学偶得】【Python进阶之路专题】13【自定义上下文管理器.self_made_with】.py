# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

class OurOpenFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    # exc_type: exception 's class
    # exc_val: exception instance
    # exc_tb: traceback object
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


# with OurOpenFile('test.txt') as f:
#     f.write('Hello , I am William form lexueoude.com')

oof = OurOpenFile('test.txt')
print(oof)

# print(oof.file)

#进入一个context（上下文），你可以认为它 __enter__ （进入了），返回的恰恰是这个file
with oof as the_oof_file:
    the_oof_file.write('test.txt')

# 跳出了context，就会__exit__（退出），然后就会关闭这个file

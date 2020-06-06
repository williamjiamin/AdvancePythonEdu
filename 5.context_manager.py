# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

with open('test.txt', 'w') as our_open_file:
    our_open_file.write('Welcome to lexueoude.com. I am William.')

# 执行完with 之后，our_open_file自动进行了关闭，所以会报I/O错误
our_open_file.read()

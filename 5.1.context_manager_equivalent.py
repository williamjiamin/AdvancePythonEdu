# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

file = open('test.txt', 'w')
try:
    file.write('Welcome to lexueoude.com. I am William.')
finally:
    file.close()

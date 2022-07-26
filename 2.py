#输出字符串
print('helloworld')
print("helloworld")

#输出含运算符的表达式
print(1 + 2)

#输出到文件，1 所指定的盘符要存在 2 使用file=fp 的格式
fp = open('e:/text.txt', 'a+')
#a+代表文件不存在则创建，存在则在原有内容后追加
print('helloworld', file=fp)
fp.close()

#不换行输出
print('hello', 'world', 'python')

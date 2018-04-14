#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：test.py

# if True:
#     print "Answer"
#     print "True"
# else:
#         print "Answer"
#         # 没有严格缩进，在执行时会报错
#         print "False"
#
# # raw_input("\n\nPress the enter key to exit.")
#
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
#
# x="a"
# y="b"
# # 换行输出
# print x
# print y
#
# print '---------'
# # 不换行输出
# print x,
# print y
#
# counter = 100 # 赋值整型变量
# miles = 1000.0 # 浮点型
# name = "John" # 字符串
#
# print counter
# print miles
# print name
#
# print '___________'
#
# s = 'ilovepython'
# print s[1:5]
# print '___________'
# print s[-3:-1]
#
# str = 'Hello World!'
#
# print str           # 输出完整字符串
# print str[0]        # 输出字符串中的第一个字符
# print str[2:5]      # 输出字符串中第三个至第五个之间的字符串
# print str[2:]       # 输出从第三个字符开始的字符串
# print str * 2       # 输出字符串两次
# print str + "TEST"  # 输出连接的字符串
#
#
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']
#
# print '___________'
# print list               # 输出完整列表
# print list[0]            # 输出列表的第一个元素
# print list[1:3]          # 输出第二个至第三个的元素
# print list[2:]           # 输出从第三个开始至列表末尾的所有元素
# print tinylist * 2       # 输出列表两次
# print list + tinylist    # 打印组合的列表

# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
#
# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
#
#
# print dict['one']          # 输出键为'one' 的值
# print dict[2]              # 输出键为 2 的值
# print tinydict             # 输出完整的字典
# print tinydict.keys()      # 输出所有键
# print tinydict.values()    # 输出所有值
#
# n=10
#
# print type(n)
# print type(dict['one'])
#
# a = 111
# print isinstance(a, int)


# a = 21
# b = 10
# c = 0
#
# c = a + b
# print "1 - c 的值为：", c
#
# c = a - b
# print "2 - c 的值为：", c
#
# c = a * b
# print "3 - c 的值为：", c
#
# c = a / float(b)
# print "4 - c 的值为：", c
#
# c = a % b
# print "5 - c 的值为：", c
#
# # 修改变量 a 、b 、c
# a = 2
# b = 3
# c = a**b
# print "6 - c 的值为：", c
#
# a = 11
# b = 5
# c = a//b
# print "7 - c 的值为：", c
#
# a=4444444; b=4444444;   # 写在同一行
# print c is d
# print c == d
# #
# #
# c = 2222222222222222222222222222.0   # 写在不同一行
# d = 2222222222222222222222222222.0   # 写在不同一行
# print c is d
# print c == d

# a = "abc"
# b = "abc"
# print a is b
# print a == b

#
# a = [1, 2, 3]
# b = a
#
# print '___________'
#
# print b is a
# print b == a
# print '___________'
#
# b = a[:]
# print b is a
# print b == a


# def printme( str ):
#     "打印传入的字符串到标准显示设备上"
#     print str
#     return
#
# a=[1,2,3]
#
# b="Runoob"
#
# printme("hello python!")
# printme(type(a))
# printme(b)


# def ChangeInt( a ):
#     a = 10
#
# b = 2
# ChangeInt(b)
# print b # 结果是 2


# # 可写函数说明
# def changeme( mylist ):
#     "修改传入的列表"
#     mylist.append([1,2,3,4]);
#     print "函数内取值: ", mylist
#     return
#
# # 调用changeme函数
# mylist = [10,20,30];
# changeme( mylist );
# print "函数外取值: ", mylist

# 可写函数说明
# def printinfo( arg1, *vartuple ):
#     "打印任何传入的参数"
#     print "输出: "
#     print arg1
#     for var in vartuple:
#         print var
#     return;
#
# # 调用printinfo 函数
# printinfo( 10 );
# printinfo( 70, 60, 50 );

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name:(blank')

print('hello')

a = 123111111111111111
b = 123111111111111111
c = 123
print(id(a))
print(id(b))
print(id(c))


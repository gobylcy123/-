#用户输入个人信息
rolername = input("请输入数字人的名字:")
rolejob = input("请输入数字人的职业:")
rolerhobby = input("请输入数字人的爱好:")
#********** Begin *********#
#定义一个显示函数命名为show_metainfo
#定义三个参数分别接收名字，职业，爱好
def show_metainfo(name,job,hobby):
    print('名字：', name)
    print('职业：', job)
    print('爱好：', hobby)
#调用函数show_metainfo
show_metainfo(rolername,rolejob,rolerhobby)
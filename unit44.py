#用户输入个人信息
rolername = input("请输入数字人的名字:")
rolejob = input("请输入数字人的职业:")
rolerhobby = input("请输入数字人的爱好:")
rolernationality = input("请输入数字人的国籍:")

#********** Begin *********#
#修改show_metainfo函数，添加一个默认参数，参数名为nationality,默认值=中国
def show_metainfo(name,job,hobby,nationality = '中国'):
    print('名字：', name)
    print('职业：', job)
    print('爱好：', hobby)
    print('国籍',nationality)
#调用函数show_metainfo
show_metainfo(rolername,rolejob,rolerhobby)
show_metainfo(rolername,rolejob,rolerhobby,rolernationality)
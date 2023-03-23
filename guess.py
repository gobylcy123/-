import random
while True:
    try:
        str_num = input('input a number:')
        num = float(str_num)
        print("你输入的是：{}".format(num))
        break   #若输入的正确，则退出，错误执行except下面代码
    except:
        print('您输入的内容不是数字，请重新输入：')
#第一步：用户出拳

user=int(input("用户出拳："))

if user==1:
    print("你出拳：石头。")
elif user==2:
    print("你出拳：剪刀。")
elif user==3:
    print("你出拳：布。")
else:

    print("你出拳：错误")
#第二步：电脑出拳1

com=random.randint(1,3)
if com==1:
    print("电脑出拳：石头。")
elif com==2:
    print("电脑出拳：剪刀。")
elif com==3:
    print("电脑出拳：布。")
    #第三步：判断胜负
if user==com:
    print("平局，大家出拳一样。")
elif (user==1 and com==2 or user==2 and com==3 or user==3 or com==1):
    print("用户获胜。")
else :
    print("电脑获胜。")
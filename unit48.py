# def count_down(start):
#     """ Count down from a number  """
#     print(start)

#     # 下一个数字大于 0 时继续调用
#     next = start - 1
#     if next > 0:
#         count_down(next)

# count_down(3)

# def reverse(s):
#     if s=='':
#         print(s)
#         return s
#     else: 
#         print(s[1:])   
#         print(s)         
#         return reverse(s[1:]) + s[0]
# str = input('请输入要给字符串')
# print(reverse(str))

#定义一个函数，求1+2+3+4+5+...个数的和
# def sum(n):
#     sum_result = 0
#     for i in range(1,n+1):
#       sum_result = sum_result + i
#     return sum_result

# n = int(input('请输入一个整数'))
# print('从1加到%d的和为%d'%(n,sum(n)))

# # 计算阶乘：根据用户输入的整数n，计算并输出n的阶乘值
# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n * fact(n-1)

# num = eval(input('请输入一个整数'))
# print("%d的阶乘结果是%d"%(num,fact(num)))

#定义一个函数，求1+2+3+4+5+...个数的和
def sum(n):         
        #########begin 从此处开始完善代码############
        #书写递归停止自我调用的条件,当n=1时，求和结果为1
        if n==1:
             return 1;
       #函数进行自我调用 sum(n) = n + sum(n-1)
        else:
            return n + sum(n-1)
        #################  end    ####################
num = int(input('请输入一个整数'))
print('从1加到%d的和为%d'%(num,sum(num))) 
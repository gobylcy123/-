#get_newprice(price,discount) 计算折后价格 price原价，discount 折扣率
def get_newprice(price,discount): 
    return price * (1-discount)
print('女上衣A的折后价',get_newprice(price = 200,discount = 0.2)) #指定关键字参数
print('发饰A',get_newprice(discount = 0.15,price = 20)) #指定关键字参数，可以调整参数位置


# def greet(name='there', message='Hi'):
#     return f"{message} {name}"

# print(greet('bobo','come on'))
# print(greet(name='bobo',message='come on'))
# print(greet(message='come on',name='bobo'))
# # print(greet(name='bobo','come on'))
# print(greet(message='come on'))
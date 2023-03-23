# 时间记录表数据
timelist = [4200,2000,4000,9000,10000]
#######   begin  在此处完善代码  ########
# 定义一个时间转换函数为conver
def convert(sec):
   hour = sec // 3600  #秒数整除3600，得时
   min = sec % 3600 // 60  #秒数求余36000，再整除60，得分
   sec %= 60 #秒数求余60得秒
   return  "%02d:%02d:%02d" % (hour, min, sec)         # 时间格式 "%02d:%02d:%02d" % (hour, min, sec) 

for value in range(len(timelist)): #循环遍历时间列表
     timelist[value] = convert(timelist[value]) #将转换的时间格式赋值到时间列表中
print(timelist) #输出时间列表
#######   end########
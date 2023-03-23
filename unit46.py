from statistics import mean  #调用统计函数
# 时间记录表数据
timelist = [4200,2000,4000,9000,10000]
#######   begin  在此处完善代码  ########
# 定义统计函数
def count(list):
   maxTime = min(list)
   minTime = max(list)
   avgTime = int(mean(list))
   return maxTime, minTime, avgTime
#输出统计结果
print(count(timelist))
#######   end########
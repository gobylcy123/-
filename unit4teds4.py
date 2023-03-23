racingPoints = {'fish': 40, 'pork': 35, 'potato': 45, 'noodles': 10}

def sort_racingPoint(disc):
    newdisc =  {}
    for value in sorted(disc.values()):
        print(sorted(disc.values()))
        print(disc.keys())
        for key  in disc.keys():
            print(disc[key])
            if disc[key] == value:
                newdisc.update({key:disc[key]})
    return newdisc
       
       

def max_Points(disc):
    for key, value in disc.items():
        if(value == max(disc.values())):
            print(key, value)
    #方法2
    #values = disc.values()
    #values.sort()
    #print(values[len(values) - 1])

def sort_new(disc):    
    return(sorted(disc.items(),key=lambda x:x[1]))

def sort_listmethod(disc):
    # 将键值以列表的方式存放
    ls  = list(disc.items()) 
    print(ls)
    ls.sort(key=lambda x:x[1])
    return ls

# print(sort_racingPoint(racingPoints))
print(sort_new(racingPoints))
# print(sort_listmethod(racingPoints))


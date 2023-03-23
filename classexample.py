class TVshow:
    list_file = ['战狼2','夺冠','西游记女儿国','熊出没','变形记']
    def __init__(self,show):
        self.__show = show
    @property
    def show(self):
        return self.__show
    @show.setter
    def show(self,value):
        if value in TVshow.list_file:
            self.__show = "您选择了《" + value + "》，稍后将播放"
        else:
            self.__show = "您点播的电影不存在"
tvshow = TVshow('战狼2')
print("正在播放：《",tvshow.show,"》")
print("你可以从",tvshow.list_file,"中选择点播电影")
tvshow.show = "夺冠"
print(tvshow.show)
import random
from Assembly import Ass
from Test_data import Num_part

class wolf:
    def __init__(self,Lis,minx,maxx,position=None):
        '''
        :param Lis: 传入的是各零件的个数，例如本文的实验中主轴有6个，齿轮1、齿轮2分别有10个，则Lis=[6,10,10]
        minx,maxx:分别表示每个元素的取值范围
        '''
        self.Lis=Lis
        if position==None:
            self.Position = []
            for i in Lis:       #这里参考我写的程序说明中的编码方式
                Pi=[]
                for j in range(i):
                    Pi.append(((maxx - minx) * random.random() + minx))
                self.Position.append(Pi)
        else:
            self.Position=position
        self.fit()

    def Decode(self):
        #按照程序说明中的解码部分进行理解
        Pos_change=[]
        for Pi in self.Position:
            Posi=dict(enumerate(Pi))
            Posi = sorted(Posi.items(), key=lambda x: x[1], reverse=True)
            Pos_change.append(Posi)

        min_l=min(self.Lis)     #找出最小的零件个数，即最多可装配min_l个装配体

        selective_scheme=[]     #选配方案
        for i in range(min_l):
            Parts=[]
            for j in range(len(Pos_change)):
                pc=Pos_change[j][i][0]
                Parts.append(pc)
            selective_scheme.append(Parts)
        return selective_scheme

    def fit(self):
        selective_scheme=self.Decode()

        #判断组合是否满足封闭尺寸链

        Meet_quality=[]             #存入满足封闭尺寸链的零件组合
        Use_parts=[]                #参与使用的零件
        for Si in selective_scheme:
            Part_Lis=[]             #一组零件组合
            for i in range(len(Si)):
                if i==0:
                    Part_Lis.append(Ass.Spindles[Si[i]])    #主轴
                elif i==1:
                    Part_Lis.append(Ass.Gear1s[Si[i]])      #齿轮1
                else:
                    Part_Lis.append(Ass.Gear2s[Si[i]])      #齿轮2

            if Ass.Dimension_chain(Part_Lis[0],Part_Lis[1],Part_Lis[2]):    #判断是否满足封闭尺寸链
                Meet_quality.append(Part_Lis)
                Use_parts.extend(Part_Lis)
        Loss=Ass.Quality_loss_fun(Meet_quality)
        C=Ass.Cost_of_surplus_parts(Use_parts)
        self.fitness=Loss+C

w=wolf(Num_part,-2,2)       #在这里，minx,maxx取-2，2








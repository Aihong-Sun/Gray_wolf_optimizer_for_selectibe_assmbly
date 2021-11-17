

#机床主轴类
class Spindle:
    def __init__(self,name,A0,target_D1,target_D2,D1,D2,Processing_cost,y1,y2,r=None):
        self.Nam=name
        self.A0=A0
        self.target_D1=target_D1
        self.target_D2=target_D2
        self.D1=D1
        self.D2=D2
        self.Processing_cost=Processing_cost
        self.y1=y1
        self.y2=y2
        self.r=0.5*self.A0      #回收价格，即原文中的r和f,这里设置为原文的一半，当然，也可以通过上面的r传参进来

#齿轮类
class Gear:
    def __init__(self,name,A0,target_D,D,Processing_cost,y,r=None):
        self.Nam=name
        self.A0=A0
        self.target_D=target_D
        self.D=D
        self.Processing_cost=Processing_cost
        self.y=y
        self.r=0.5*self.A0
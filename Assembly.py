from Test_data import A0,target_size,Size,Cost,delta_y,Nam_Lis
from parts import Spindle,Gear

class Assemble:
    def __init__(self,A0,target_size,Size,Cost,delta_y,Nam_Lis):
        self.Nam_Lis=Nam_Lis
        self.delta_y=delta_y
        self.A0=A0
        self.target_size=target_size
        self.Size=Size
        self.Cost=Cost
        self.Create_parts()
        self.Tdelta_t=0.020     #这个根据原文要求所定，即最大间隙不应超过0.020mm.

    def Create_parts(self):
        self.Spindles=[]         #里面装CAK6150主轴类
        self.Gear1s=[]           #里面装02065L1齿轮类
        self.Gear2s=[]           #里面装02405L齿轮类
        for i in range(len(self.A0)):
            if i==0:        #第一位为主轴
                for j in range(len(self.Cost[i])):
                    Sp=Spindle(self.Nam_Lis[i][j],self.A0[i],self.target_size[i][0],self.target_size[i][1],
                               self.Size[i][0][j],self.Size[i][1][i],self.Cost[i][j],self.delta_y[i][0],self.delta_y[i][1])
                    self.Spindles.append(Sp)
            elif i==1:
                for k in range(len(self.Cost[i])):
                    g1=Gear(self.Nam_Lis[i][k],self.A0[i],self.target_size[i][0],self.Size[i][0][k],self.Cost[i][k],self.delta_y[i][0])
                    self.Gear1s.append(g1)
            else:
                for k in range(len(self.Cost[i])):
                    g2=Gear(self.Nam_Lis[i][k],self.A0[i],self.target_size[i][0],self.Size[i][0][k],self.Cost[i][k],self.delta_y[i][0])
                    self.Gear2s.append(g2)

    #封闭环尺寸链约束函数
    def Dimension_chain(self,S,G1,G2):
        '''
        :param S: 为一个主轴类
        :param G1: 为齿轮1类
        :param G2: 为齿轮2类
        :return delta_t: 封闭尺寸偏差
        '''
        t1=S.D1-G1.D
        t2=S.D2-G2.D
        T1=bool(t1<=self.Tdelta_t)
        T2=bool(t2<=self.Tdelta_t)
        if T1 and T2:
            return True     #如何满足装配尺寸链要求，返回True
        else:
            return False

    #质量损失成本函数
    def Quality_loss_fun(self,Lis):
        '''
        :param Lis: 
        :return Loss: 
        '''
        Loss=0
        for i in range(len(Lis)):
            for j in range(len(Lis[i])):
                if j==0:        #当部件为主轴时
                    k1=Lis[i][j].A0/Lis[i][j].y1
                    k2=Lis[i][j].A0/Lis[i][j].y1
                    L_y1=k1*pow((Lis[i][j].D1-Lis[i][j].target_D1),2)          #
                    L_y2 = k2 * pow((Lis[i][j].D2 - Lis[i][j].target_D2),2)   #
                    Loss=Loss+L_y1+L_y2
                else:
                    k=Lis[i][j].A0/Lis[i][j].y
                    L_y = k * (Lis[i][j].D - Lis[i][j].target_D)
                    Loss+=L_y
        return Loss

    #剩余件成本函数
    def Cost_of_surplus_parts(self,Lis):
        '''
        :param Lis: 
        :return: 
        '''
        Ji=0        #参与装配的再制造件i的加工成本
        for Li in Lis:
            Ji+=Li.Processing_cost


        G=0         #未参与装配的再制造件及再利用件的剩余再制造零件的总成本
        for Si in self.Spindles:
            if Si not in Lis and 'N'not in Si.Nam:  #判断主轴是再利用或再制造件且没有被利用的件
                G+=Si.r

        for Sj in self.Gear1s:
            if Sj not in Lis and 'N' not in Sj.Nam:  # 判断齿轮1是再利用或再制造件且没有被利用的件
                G += Sj.r

        for Sk in self.Gear2s:
            if Sk not in Lis and 'N' not in Sk.Nam:  # 判断齿轮1是再利用或再制造件且没有被利用的件
                G += Sk.r
        C=Ji+G
        return C

    def show(self,Lis):
        for i in range(len(Lis)):
            print('第',i+1,'个零件组合')
            for j in range(len(Lis[i])):
                if j==0:
                    print(self.Spindles[Lis[i][j]].Nam)
                elif j==1:
                    print(self.Gear1s[Lis[i][j]].Nam)
                else:
                    print(self.Gear2s[Lis[i][j]].Nam)


Ass=Assemble(A0,target_size,Size,Cost,delta_y,Nam_Lis)






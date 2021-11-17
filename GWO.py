import random
from wolf import w,Num_part
import copy
from wolf import wolf
from Assembly import Ass


class GWO:

    def __init__(self,pop_size,max_iter,Lis):
        self.pop_size=pop_size      #狼群数量
        self.max_iter=max_iter      #最大迭代次数
        self.minx=-2
        self.maxx=2
        self.Lis=Lis

    # 灰狼优化算法
    def main(self):
        rnd = random.Random(0)

        # 创建狼群
        population = [w for i in range(self.pop_size)]

        # 基于狼的适应值
        # 按升序对总体进行排序
        population = sorted(population, key=lambda temp: temp.fitness)

        # 将种群中适应度最高的三头狼命名为alpha_wolf, beta_wolf和gama_wolf
        alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])

        #迭代开始
        Iter = 0
        while Iter < self.max_iter:

            # 每隔10次迭代，输出当前迭代次数和当前最优的适应度
            if Iter % 1 == 0 and Iter > 1:
                print("Iter = " + str(Iter) + " best fitness = %.3f" % alpha_wolf.fitness)

            # 从2线性减少到0
            a = 2 * (1 - Iter / self.max_iter)

            # 在三匹头狼的帮助下更新狼群中其他成员
            for i in range(self.pop_size):
                A1, A2, A3 = a * (2 * rnd.random() - 1), a * (
                    2 * rnd.random() - 1), a * (2 * rnd.random() - 1)
                C1, C2, C3 = 2 * rnd.random(), 2 * rnd.random(), 2 * rnd.random()


                Xnew=[]
                for pi in range(len(alpha_wolf.Position)):
                    X1 = []
                    X2 = []
                    X3 = []
                    xnew = []
                    for j in range(len(alpha_wolf.Position[pi])):
                        x1= alpha_wolf.Position[pi][j] - A1 * abs(
                        C1 - alpha_wolf.Position[pi][j] - population[i].Position[pi][j])

                        x2 = beta_wolf.Position[pi][j] - A1 * abs(
                            C1 - beta_wolf.Position[pi][j] - population[i].Position[pi][j])

                        x3 = gamma_wolf.Position[pi][j] - A1 * abs(
                            C1 - gamma_wolf.Position[pi][j] - population[i].Position[pi][j])

                        x4=(x1+x2+x3)/3
                        xnew.append(x4)
                    Xnew.append(xnew)

                #狼的新位置
                new_wolf=wolf(self.Lis,self.minx,self.maxx,Xnew)
                # 计算新解的适应度函数
                fnew = new_wolf.fitness

                # 贪婪搜索
                if fnew < population[i].fitness:
                    population[i] = new_wolf

            # On the basis of fitness values of wolves
            # sort the population in asc order
            population = sorted(population, key=lambda temp: temp.fitness)

            # best 3 solutions will be called as
            # alpha, beta and gama
            alpha_wolf, beta_wolf, gamma_wolf = copy.copy(population[: 3])

            Iter += 1
        # end-while

        # 返回最优解
        return alpha_wolf


g=GWO(100,100,Num_part)
wolf=g.main()
Lis=wolf.Decode()
Ass.show(Lis)


#!/usr/bin/env python
# encoding: utf-8
# @file: mGAPSO.py
# @desc:a micro-EA embeded in PSO

from config import test_funcs
from PSO import PSO
import math

dim = 30    #   粒子维度
size = 30   #   种群大小
iter_num1 = 10  #   迭代次数
iter_num2 = 500 # mGA循环次数
max_vel = 0.6   #   最大速度
func_id = 10    #   函数序号
mu = 0
sigma =1


def corr(p1, p2):
    '''
    直方图相关图计算
    :param p1:
    :param p2:
    :return:
    '''
    avg1 = sum(p1)/len(p1)
    avg2 = sum(p2)/len(p2)
    para1 = 0
    para2 = 0
    for i in range(len(p1)):
        para1 += (p1[i]-avg1)*(p2[i]-avg2)
        para2 += ((p1[i]-avg1)**2)*((p2[i]-avg2)**2)
    return para1/para2

if __name__ == '__main__':
    pso = PSO(dim, size, iter_num1, test_funcs[func_id]['bound'], max_vel, W=0.78,C1=1.2,
              C2=1.2, fit_func=test_funcs[func_id]['func'], mu =mu, sigma =sigma)
    pso.update()
    first_particles = pso.first_particles
    best_particle = pso.best_particle
    sig = True
    change_count = 0 # 用于计数，判断在50次循环内是否有过更新
    iter_count = 0
    while True:
        if change_count >= 50 and iter_count >= iter_num2:  # 若超过50次循环最优没有改变且迭代次数大于500，则退出循环
            break
        sorted_fps = sorted(first_particles, key=lambda p:corr(p.get_pos(),best_particle.get_pos()), reverse=sig)
        sig = not sig
        parts = sorted_fps[:4]+[best_particle]
        sep_n = int(len(best_particle.get_pos())/5)
        mp_pos = []
        mp_vel = []
        for j in range(5):
            # 对粒子分为五份，分别进行PSO操作
            mpso = PSO(sep_n,5,iter_num1,test_funcs[func_id]['bound'], max_vel, W=1/(2*math.log10(2.0)),C1=0.5+math.log10(2.0),
                       C2=0.5+math.log10(2.0), fit_func=test_funcs[func_id]['func'], mu =mu, sigma =sigma, is_mpso=True)
            for k in range(5):
                # 对mPSO群中粒子迭代，更新其位置
                mpso.Particle_list[j].pos = parts[k].get_pos()[j*sep_n: (j+1)*sep_n]
                mpso.Particle_list[j].vel = parts[k].get_vel()[j*sep_n: (j+1)*sep_n]
                mpso.Particle_list[j].update_fv()
            mpso.update()
            best_mp = mpso.best_particle
            mp_pos += best_mp.pos
            mp_vel += best_mp.vel
        if test_funcs[func_id]['func'](mp_pos) < best_particle.get_fitness_value():
            best_particle.pos = mp_pos
            best_particle.vel = mp_vel
            best_particle.update_fv()
            change_count = 0
        else:
            change_count += 1
        iter_count += 1
    print('最优解为：', best_particle.get_fitness_value())

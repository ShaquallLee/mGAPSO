#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: mGAPSO.py
# @time: 2020/7/27 0027 15:31
# @desc:a micro-EA embeded in PSO

import numpy as np
import matplotlib.pyplot as plt
from config import test_funcs
from PSO import PSO
import math

dim = 30
size = 50
iter_num1 = 10
iter_num2 = 500 # mGA循环次数
max_vel = 10
func_id = 10
mu = 0
sigma =10


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
    pso = PSO(dim, size, iter_num1, test_funcs[func_id]['bound'], max_vel, W=1/(2*math.log10(2.0)),C1=0.5+math.log10(2.0),
              C2=0.5+math.log10(2.0), fit_func=test_funcs[func_id]['func'], mu =mu, sigma =sigma)
    pso.update()
    first_particles = pso.first_particles
    best_particle = pso.best_particle
    sig = True
    for i in range(iter_num2):
        sorted_fps = sorted(first_particles, key=lambda p:corr(p.get_pos(),best_particle.get_pos()), reverse=sig)
        sig = not sig
        parts = sorted_fps[:4]+[best_particle]
        sep_n = len(best_particle.get_pos())/5
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
    print('最优解为：',best_particle.get_fitness_value())
    # print("最优位置:" + str(best_pos))
    # print("最优解:" + str(fit_var_list[-1]))
    # plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list)
    # plt.show()

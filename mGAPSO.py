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
iter_num2 = 100
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
    pso = PSO(dim, size, iter_num1, test_funcs[func_id]['bound'], max_vel, W=1/(2*math.log10(2.0)),C1=0.5+math.log10(2.0),C2=0.5+math.log10(2.0), fit_func=test_funcs[func_id]['func'], mu =mu, sigma =sigma)
    _, _ = pso.update()
    first_particles = pso.first_particles
    best_particle = pso.best_particle
    sig = True
    for i in range(iter_num2):
        if sig:
            sorted_fps = sorted(first_particles, key=lambda p:corr(p.get_pos(),best_particle.get_pos()), reverse=True)
        else:
            sorted_fps = sorted(first_particles, key=lambda p: corr(p.get_pos(), best_particle.get_pos()), reverse=False)
        parts = sorted_fps[:4]+[best_particle]
        sep_n = len(best_particle.get_pos())/5
        for j in range(5):

    # print("最优位置:" + str(best_pos))
    # print("最优解:" + str(fit_var_list[-1]))
    # plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list)
    # plt.show()

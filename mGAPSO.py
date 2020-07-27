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
iter_num = 2000
max_vel = 10
func_id = 10
mu = 0
sigma =10

if __name__ == '__main__':
    pso = PSO(dim, size, iter_num, test_funcs[func_id]['bound'], max_vel, W=1/(2*math.log10(2.0)),C1=0.5+math.log10(2.0),C2=0.5+math.log10(2.0), fit_func=test_funcs[func_id]['func'], mu =mu, sigma =sigma)
    fit_var_list, best_pos = pso.update()
    print("最优位置:" + str(best_pos))
    print("最优解:" + str(fit_var_list[-1]))
    plt.plot(np.linspace(0, iter_num, iter_num), fit_var_list)
    plt.show()

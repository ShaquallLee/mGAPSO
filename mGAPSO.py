#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: mGAPSO.py
# @time: 2020/7/27 0027 15:31
# @desc:

from PSO import PSO

dim = 30
size = 30
iter_num = 1500
x_max = 100
max_vel = 20


if __name__ == '__main__':
    pso = PSO(dim, size, iter_num, x_max, max_vel, C1, C2, W, fit_func, mu =mu, sigma =sigma)

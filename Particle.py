#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: Particle.py
# @time: 2020/8/1 0001 9:37
# @desc:

import random

class Particle:
    # 初始化
    def __init__(self, x_max, max_vel, dim, fit_fun, is_mpso):
        self.pos = [random.uniform(-x_max, x_max) for i in range(dim)]  # 粒子的位置
        self.vel = [random.uniform(-max_vel, max_vel) for i in range(dim)]  # 粒子的速度
        self.__bestPos = [0.0 for i in range(dim)]  # 粒子最好的位置
        self.__fitnessValue = fit_fun(self.pos)  # 适应度函数值
        if is_mpso:
            self.__everBestValues = []
        else:
            self.__everBestValues = [fit_fun(self.pos)]  # 粒子曾经最好的适应值
        self.__everBestPos = [] # 粒子曾经最好的位置
        self.__fitFun = fit_fun

    def update_fv(self, ):
        self.__fitnessValue = self.__fitFun(self.pos)
        self.__everBestValues.append(self.__fitnessValue)

    def set_pos(self, i, value):
        self.pos[i] = value

    def get_pos(self):
        return self.pos

    def set_best_pos(self, i, value):
        self.__bestPos[i] = value

    def get_best_pos(self):
        return self.__bestPos

    def set_vel(self, i, value):
        self.vel[i] = value

    def get_vel(self):
        return self.vel

    def set_fitness_value(self, value):
        self.__fitnessValue = value

    def set_fitness_value2(self, value):
        self.__fitnessValue = value
        self.__everBestValues.append(value)

    def get_fitness_value(self):
        return self.__fitnessValue

    def get_ever_best_values(self):
        return self.__everBestValues

    def set_ever_best_values(self, item):
        self.__everBestValues.append(item)

    def get_ever_best_pos(self):
        return self.__everBestPos

    def set_ever_best_pos(self, pos):
        self.__everBestPos.append(pos)


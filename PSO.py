#!/usr/bin/env python
# encoding: utf-8
# @file: PSO.py
# @desc:novel PSO algrithm

import random
from Particle import Particle
from tools import boxmullersampling

class PSO:
    def __init__(self, dim, size, iter_num, x_max, max_vel, C1, C2, W, fit_func, best_fitness_value=float('Inf'),mu=0.0, sigma=1.0, is_mpso=False):
        self.C1 = C1
        self.C2 = C2
        self.W = W
        self.dim = dim  # 粒子的维度
        self.size = size  # 粒子个数
        self.iter_num = iter_num  # 迭代次数
        self.x_max = x_max
        self.mu = mu
        self.sigma = sigma
        self.max_vel = max_vel  # 粒子最大速度
        self.best_fitness_value = best_fitness_value
        self.best_position = [0.0 for i in range(dim)]  # 种群最优位置
        self.best_particle = None   #种群最优的粒子
        self.fitness_val_list = []  # 每次迭代最优适应值
        self.fit_function = fit_func #适应度函数

        # 对种群进行初始化
        self.Particle_list = [Particle(self.x_max, self.max_vel, self.dim, self.fit_function, is_mpso) for i in range(self.size)]
        self.first_particles = self.Particle_list

    def set_bestFitnessValue(self, value):
        self.best_fitness_value = value

    def set_bestParticle(self, particle):
        self.best_particle = particle

    def get_bestFitnessValue(self):
        return self.best_fitness_value

    def set_bestPosition(self, i, value):
        self.best_position[i] = value

    def get_bestPosition(self):
        return self.best_position

    # 更新速度
    def update_vel(self, part):
        everBestPos = part.get_ever_best_pos()
        for i in range(self.dim):
            cou = 0
            psum = 0
            for pi in everBestPos:
                psum += pi[i]
                cou += 1
            if cou == 0:
                pp = 0
            else:
                pp = float(psum)/cou
            vel_value = self.W * part.get_vel()[i] + self.C1 * random.random() * (pp - part.get_pos()[i]) \
                        + self.C2 * random.random() * (self.get_bestPosition()[i] + 2*self.x_max*boxmullersampling(mu=self.mu, sigma=self.sigma) - part.get_pos()[i])
            if vel_value > self.max_vel:
                vel_value = self.max_vel
            elif vel_value < -self.max_vel:
                vel_value = -self.max_vel
            part.set_vel(i, vel_value)

    # 更新位置
    def update_pos(self, part):
        for i in range(self.dim):
            pos_value = part.get_pos()[i] + part.get_vel()[i]
            if pos_value < -self.x_max:
                pos_value = 2 * (-self.x_max) - pos_value
                part.set_vel(i, -part.get_vel()[i])
            if pos_value > self.x_max:
                pos_value = 2* self.x_max - pos_value
                part.set_vel(i, -part.get_vel()[i])
            part.set_pos(i, pos_value)

        value = self.fit_function(part.get_pos())
        if value < part.get_fitness_value():
            part.set_fitness_value2(value)
            for i in range(self.dim):
                part.set_best_pos(i, part.get_pos()[i])
            part.set_ever_best_pos(part.get_best_pos())
        if value < self.get_bestFitnessValue():
            self.set_bestFitnessValue(value)
            self.set_bestParticle(part)
            for i in range(self.dim):
                self.set_bestPosition(i, part.get_pos()[i])

    def update(self):
        for i in range(self.iter_num):
            for part in self.Particle_list:
                self.update_vel(part)  # 更新速度
                self.update_pos(part)  # 更新位置
            # print(i, ': ', self.get_bestFitnessValue())
            self.fitness_val_list.append(self.get_bestFitnessValue())  # 每次迭代完把当前的最优适应度存到列表
        return self.fitness_val_list, self.get_bestPosition()


#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: tools.py
# @time: 2020/8/1 0001 9:40
# @desc:

import numpy as np

def boxmullersampling(mu=0, sigma=1, size=1):
    '''
    产生一个高斯函数随机数
    :param mu:
    :param sigma:
    :param size:
    :return:
    '''
    u = np.random.uniform(size=size)
    v = np.random.uniform(size=size)
    z = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * v)
    return mu + z * sigma

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
    pass

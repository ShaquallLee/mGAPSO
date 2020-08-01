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


if __name__ == '__main__':
    pass

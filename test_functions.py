#!/usr/bin/env python
# encoding: utf-8
# @author: lishaogang
# @file: test_functions.py
# @time: 2020/6/21 0021 7:17
# @desc:

import math
import random


def f1(present):
    '''
    f1 = sum(xi*xi) i=1,2,......,30
    :param present:x
    :return:
    '''
    ret = 0
    for d in range(len(present)):
        ret += present[d]*present[d]
    return ret

def f2(present):
    '''
    f2 = min(sum(|xi|) + multi(|xi|)) i=1,2,......,30
    :param present:
    :return:
    '''
    sum = 0
    multi = 1
    for d in range(len(present)):
        sum += abs(present[d])
        multi *= abs(present[d])
    return sum + multi

def f3(present):
    '''
    f3=sum(i=1,n)[sum(j=1,i : xj)]^2 n=30
    :param present:
    :return:
    '''
    ret = 0
    for i in range(len(present)):
        x = 0
        for j in range(i+1):
            x += present[j]
        ret += x*x
    return ret

def f4(present):
    '''
    f4 =	max(|xi|) i=1,2......30
    :param present:
    :return:
    '''
    ret = present[0]
    for d in range(len(present)):
        x = abs(present[d])
        if ret < x:
            ret = x
    return ret

def f5(present):
    '''
    f5 = sum(1,n-1 : (100(Xi+1 - Xi^2)^2 + (Xi-1)^2))
    :param present:
    :return:
    '''
    ret = 0
    for d in range(len(present)-1):
        ret += 100 * math.pow((present[d+1]-present[d]*present[d]),2) + math.pow((present[d]-1),2)
    return ret

def f6(present):
    '''
    f6 = sum(floor((xi+0.5)*(xi+0.5)) i=1,2,......,30
    :param present:
    :return:
    '''
    ret = 0
    for d in range(len(present)):
        t = math.floor(present[d]+0.5)
        ret += t*t
    return ret

def f7(present):
    '''
    f7 = sum(1:n i*xi^4) + random[0,1)
    :param present:
    :return:
    '''
    ret = 0
    for d in range(len(present)):
        ret += (d+1)*math.pow(present[d],4)
    ret += random.uniform(0,1)
    return ret

def f8(present):
    '''
    f8 = sum(-xi*sin(sqrt(|xi|))) i=1,2,......,30
    :param present:
    :return:
    '''
    ret = 0
    for d in range(len(present)):
        ret += -present[d]*math.sin(math.sqrt(math.fabs(present[d])))
    return ret

def f9(present):
    '''
     f9 = sum(xi^2-10cos(2*pi*xi)+10) i=1,2,......,30
    :param present:
    :return:
    '''
    ret = 0
    for d in range(len(present)):
        ret += (present[d]*present[d]-10*math.cos(2*math.pi*present[d])+10)
    return ret

def f10(present):
    s1 = 0
    s2 = 0
    for d in range(len(present)):
        s1 += present[d] *present[d]
        s2 += math.cos(2*math.pi*present[d])
    ss1 = math.exp(-0.2*(s1/len(present)**0.5))
    ret = -20 * ss1- math.exp(s2/len(present))+20+math.exp(1.0)
    return ret

def f11(present):
    '''
    f11 = sum(xi*xi)/4000.0-multi(cos(xi/sqrt(i)))+1;
    :param present:
    :return:
    '''
    ret, sum, multi = 0,0,0
    for d in range(len(present)):
        sum += present[d] * present[d]
        multi *= math.cos(present[d]/math.sqrt(d+1))
    ret = sum/4000.0 - multi +1
    return ret

def U(x, a, k, m):
    if x > a:
        return k * math.pow(x-a, m)
    elif x < -a:
        return k * math.pow(-x-a, m)
    else:
        return 0

def f12(present):
    y = []
    s1, s2, multi = 0,0,1.0
    for d in range(len(present)):
        y.append(1.0 + (present[d]+1)/4.0)
    for d in range(len(present)-1):
        s1 += (y[d] - 1) * (y[d] - 1) * (1 + 10 * math.sin(math.pi * y[d+1]) * math.sin(math.pi * y[d + 1]))
        s2 += U(present[d], 10, 100, 4)
    s1 += 10 * math.sin(math.pi*y[0])*math.sin(math.pi*y[0])+math.pow(y[len(present)-1], 2)
    s1 *= math.pi/len(present)
    s2 += U(present[len(present)-1], 10, 100, 4)
    return s1 + s2

def f13(present):
    s1, s2, multi = 0,0, 1.0
    for d in range(len(present)-1):
        s1 += (present[d] - 1) * (present[d] - 1) * (1 + math.sin(3.0 * math.pi * present[d + 1]) * math.sin(3.0 * math.pi * present[d + 1]))
        s2 += U(present[d], 5, 100, 4)
    s1 += math.sin(3.0 * math.pi * present[0]) * math.sin(3.0 * math.pi * present[0])
    s1 += (present[len(present) - 1] - 1) * (present[len(present) - 1] - 1) * (1 + math.sin(2 * math.pi * present[len(present) - 1]) * math.sin(2 * math.pi * present[len(present) - 1]))
    s1 /= 10.0
    s2 += U(present[len(present) - 1], 5, 100, 4)
    return s1+s2


if __name__ == '__main__':
    a = [17.937, 30.939]
    res = f10(a)
    print(res)
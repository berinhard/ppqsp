#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import division
import sys
from timeit import Timer

divisble_by_2 = lambda x: not x % 2
pow_3 = lambda x: x ** 3
iter_list = range(0, 1000)

##########################################
######## FILTER
def filter_with_normal_for():
    l = []
    for x in iter_list:
        if divisble_by_2(x):
            l.append(x)
    return l

def filter_with_list_comprehension():
    return [x for x in iter_list if divisble_by_2(x)]

def filter_with_filter_func():
    return filter(divisble_by_2, iter_list)

##########################################
######## MAP
def map_with_normal_for():
    l = []
    for x in iter_list:
        l.append(pow_3(x))
    return l

def map_with_list_comprehension():
    return [pow_3(x) for x in iter_list]

def map_with_map_func():
    return map(pow_3, iter_list)

##########################################
######## MAP + FILTER
def mapfilter_with_normal_for():
    l = []
    for x in iter_list:
        if divisble_by_2(x):
            l.append(pow_3(x))
    return l

def mapfilter_with_list_comprehension():
    return [pow_3(x) for x in iter_list if divisble_by_2(x)]

def mapfilter_with_mapfilter_func():
    return map(pow_3, filter(divisble_by_2, iter_list))

def create_table_result(title, results):
    calc = {
        'fn': title,
        'min': min(results),
        'mean': sum(results) / len(results),
        'max': max(results)
    }
    print '\n{fn:>30s} {min:<10.8f} {mean:<10.8f} {max:<10.8f}\n'.format(**calc)

def profile(stmt='pass', setup='pass'):

    t = Timer(stmt, setup)
    r = t.repeat(10, 1000)

    create_table_result(stmt, r)

if __name__ == '__main__':

    print "***** FILTER PROFILING *****"
    assert filter_with_normal_for() == filter_with_list_comprehension() == filter_with_filter_func()
    head = 'fn min mean max'.split(' ')
    print '{0:>30s} {1:<10s} {2:<10s} {3:<10s}'.format(*head)
    profile('filter_with_normal_for()', 'from __main__ import filter_with_normal_for')
    profile('filter_with_list_comprehension()', 'from __main__ import filter_with_list_comprehension')
    profile('filter_with_filter_func()', 'from __main__ import filter_with_filter_func')

    print "***** MAP PROFILING *****"
    assert map_with_normal_for() == map_with_list_comprehension() == map_with_map_func()
    head = 'fn min mean max'.split(' ')
    print '{0:>30s} {1:<10s} {2:<10s} {3:<10s}'.format(*head)
    profile('map_with_normal_for()', 'from __main__ import map_with_normal_for')
    profile('map_with_list_comprehension()', 'from __main__ import map_with_list_comprehension')
    profile('map_with_map_func()', 'from __main__ import map_with_map_func')

    print "***** MAP + FILTER PROFILING *****"
    assert mapfilter_with_normal_for() == mapfilter_with_list_comprehension() == mapfilter_with_mapfilter_func()
    head = 'fn min mean max'.split(' ')
    print '{0:>30s} {1:<10s} {2:<10s} {3:<10s}'.format(*head)
    profile('mapfilter_with_normal_for()', 'from __main__ import mapfilter_with_normal_for')
    profile('mapfilter_with_list_comprehension()', 'from __main__ import mapfilter_with_list_comprehension')
    profile('mapfilter_with_mapfilter_func()', 'from __main__ import mapfilter_with_mapfilter_func')

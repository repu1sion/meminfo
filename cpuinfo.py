#!/usr/bin/python3

import sys
import os

# cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor


with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor') as f:
    governor = f.readline()
    print('current governor is:', governor)

with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors') as f2:
    governors = f2.readline()
    governors_list = governors.split()
    #for w in governors:
    #    governors_list.append(w)
    #    print (w)

    print('available governors are:')
    i = 1
    for g in governors_list:
        print (i,')',g)
        i += 1

    print('input number to select proper governor or [0] to return:')
    try:
        x = int(input())
    except ValueError:
        exit()

    #print('user input:', x)

    if x==0:
        exit()
    elif x > len(governors_list):
        exit()
    else:
        s1 = 'echo '
        s2 = governors_list[x-1]
        s3 = ' | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor'
        final = s1 + s2 + s3
        os.system(final)

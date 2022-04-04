#!/usr/bin/python3

import sys

def print_ram():
	# dict() constructor builds a dictionary in meminfo from key-value pairs.
    meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    mem_kib = meminfo['MemTotal']  # e.g. 3921852
    mem_free = meminfo['MemFree']
    mem_cached = meminfo['Cached']
    mem_buffers = meminfo['Buffers']
    mem_avail = meminfo['MemAvailable']
    mem_used = mem_kib - mem_free - mem_buffers - mem_cached

    print("RAM | Total: %d Mb |" % (mem_kib/1024), "Free: %d Mb |" %  (mem_free/1024),
    "Cached: %d Mb |" %(mem_cached/1024), "Used: %d Mb |" %(mem_used/1024),
    "Available: %d Mb" %(mem_avail/1024) )


'''
	with open('/proc/meminfo') as f:
		i = 0
		# int(s) for s in txt.split() if s.isdigit()
		for line in f:
			if i == 0:
				Total = line
			elif i == 1:
				Free = line
			elif i == 2:
				Avail = line
			elif i == 4:
				Cached = line
			i += 1
		#read_data = f.read()
		#print (read_data)

		print(Total)
		print(Free)
		print(Avail)
		print(Cached)
'''

#print('RAM | ')
print_ram()

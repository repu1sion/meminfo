#!/usr/bin/python3

import sys
import os

class Tool:
	x = 0

	def ping():
		os.system('ping -c 4 kernel.org')

	def uname():
		os.system('uname -a')


if __name__ == "__main__":
	print('p - ping, u - uname')

	x = input()

	if x=='p':
		Tool.ping()
	elif x=='u':
		Tool.uname()


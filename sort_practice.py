import random
import time
from functools import wraps


li = [random.randint(0, 20000) for x in range(20000)]    #随机生成一个列表

def foo(a):
	def sortTime(func):
		#装饰器，用来统计各种排序算法的时间
		@wraps(func)
		def wrapper(*args, **kwargs):
			start_time = time.time()
			res_func = func(*args, **kwargs)
			end_time = time.time()
			total_time = end_time - start_time
			print('"{0}"算法共执行{1}秒'.format(a, total_time))
			return res_func
		return wrapper
	return sortTime

@foo('选择排序')
def selectSort(li):
	#选择排序，核心思想是从左至右，不断选择剩余列表中的最小值
	n = len(li)
	if n <= 1:
		return li
	else:
		for i in range(n):
			min_index = i
			for j in range(i+1, n):
				if li[j] < li[min_index]:
					min_index = j
			li[i], li[min_index] = li[min_index], li[i]
		return li

@foo("插入排序")
def insertSort(li):
	#插入排序，核心思想是对每一个元素按照从后向前的顺序依次比较大小
	n = len(li)
	if n <= 1:
		return li
	else:
		for i in range(1, n):
			value = li[i]
			index = i
			while li[index-1] > value and index > 0:
				index -= 1
			res = li.pop(i)
			li.insert(index, res)
		return li

@foo("冒泡排序")
def bubbleSort(li):
	#冒泡排序，持续比较相邻元素，大的挪到后面，因此大的会逐步往后挪，故称之为冒泡
	n = len(li)
	if n <= 1:
		return li
	else:
		for i in range(n-1):
			for j in range(n-i-1):
				if li[j] > li[j+1]:
					li[j], li[j+1] = li[j+1], li[j]
		return li





"""
统计n=10000/20000时，各种算法需要的时间：

选择排序=8.7s/34s
插入排序=7.1s/29s
冒泡排序=22s/85s
"""	



# a = selectSort(li)
# b = insertSort(li)
c = bubbleSort(li)












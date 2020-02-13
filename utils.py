# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import factorial
from math import sqrt
from scipy.integrate import quad

def fact(n):
	# if n < 0:
	# 	raise ValueError
	# else:
	# 	return factorial(n)
	try:
		return factorial(n)
	except:
		raise ValueError('value < 0 !')

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	result = b**2 - 4 * a * c

	if result < 0:
		return ()
	elif result == 0:
		result = -b / 2 * a
		return (result,)
	else:
		result_1 = (-b + sqrt(result)) / 2 * a
		result_2 = (-b - sqrt(result)) / 2 * a
		return (result_1, result_2)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	func = lambda x:eval(function)
	result = quad(func, lower, upper)
	return round(result[0], 4)

if __name__ == '__main__':
	# print(fact(-2))
	# print(roots(1, -2, 1))
	print(integrate('x ** 2 - 1', -1, 1))

from pyparsing import *
def sin():
	
	variable=Word(nums)
	sin_op=Suppress("math.")+"sin"+Suppress("(")+variable+Suppress("/ 180.0 * math.pi")+Suppress(")")
	return sin_op

def cos():
	
	variable=Word(nums)
	cos_op=Suppress("math.")+"cos"+Suppress("(")+variable+Suppress("/ 180.0 * math.pi)")
	return cos_op

def tan():
	
	variable=Word(nums)
	tan_op=Suppress("math.")+"tan"+Suppress("(")+variable+Suppress("/ 180.0 * math.pi)")
	return tan_op

def asin():
	
	variable=Word(nums)
	asin_op=Suppress("math.")+"asin"+Suppress("(")+variable+Suppress("/ 180.0 * math.pi)")
	return asin_op

def acos():
	
	variable=Word(nums)
	acos_op=Suppress("math.")+"acos"+Suppress("(")+variable+Suppress("/ 180.0 * math.pi)")
	return acos_op

def atan():
	
	variable=Word(nums)
	atan_op=Suppress("math.")+"atan"+Suppress("(")+variable+Suppress("/ 180.0 * math.pi)")
	return atan_op


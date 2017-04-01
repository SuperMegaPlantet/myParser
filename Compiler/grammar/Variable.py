from pyparsing import *

def equal():
	variable = Word(alphanums)
	value = Word(nums)
	equation=variable+"="+value+Suppress(LineEnd())
	return equation



from pyparsing import *

def add():
	variable = Word(alphanums)
	add=variable+"="+variable+"+"+variable+Suppress(LineEnd())
	return add

def substraction():
	variable = Word(alphanums)
	add=variable+"="+variable+"-"+variable+Suppress(LineEnd())
	return add

def multiply():
	variable = Word(alphanums)
	add=variable+"="+variable+"*"+variable+Suppress(LineEnd())
	return add

def division():
	variable = Word(alphanums)
	add=variable+"="+variable+"/"+variable+Suppress(LineEnd())
	return add


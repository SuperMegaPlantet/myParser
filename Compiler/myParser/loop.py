from Bit import highValue,lowValue


def delay01(time,mode,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA4"
	list1[1]="0x01"
	list1[2]=highValue(time)
	list1[3]=lowValue(time)
	list1[4]=mode
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def delay02(time,mode,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA4"
	list1[1]="0x02"
	list1[2]=highValue(time)
	list1[3]=lowValue(time)
	list1[4]=mode
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def delay03(time,mode,a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA4"
	list1[1]="0x03"
	list1[2]=highValue(time)
	list1[3]=lowValue(time)
	list1[4]=mode
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)	
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def exitLoop(a,b):
	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA3"
	list1[1]="0x61"
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def finiteLoopEnd(num,a,b):

	#check range of loop number
	if num<41 or num>61:
		print "ERROR:Loop number is out of bound!"

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA3"
	list1[1]="0x"+str(num)
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def finiteLoopStart(num,indexs,mode,a,b):
	#check range of loop number
	if num<21 or num>40:
		print "ERROR:Loop number is out of bound!"

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA3"
	list1[1]="0x"+str(num)
	list1[2]=highValue(indexs)
	list1[3]=lowValue(indexs)
	list1[4]=mode
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;

def infiniteLoopEnd(num,a,b):
	#check range of loop number
	if num<=80 or num>100:
		print "ERROR:Loop number is out of bound!"
	##generate list 1*30
	list1=[0]*30
	#fill in variables
	list1[0]="0xA3"
	list1[1]="0x"+str(num)
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)



	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	print output_bytes
	return output_bytes;

def infiniteLoopStart(num,a,b):
	#check range of loop number
	if num>20:
		print "ERROR:Loop number is out of bound!"
	##generate list 1*30
	list1=[0]*30
	#fill in variables
	list1[0]="0xA3"
	if num<10:
		list1[1]="0x0"+str(num)
	else:
        	list1[1]="0x"+str(num)
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)



	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	print output_bytes
	return output_bytes;

def timingLoopEnd(num,a,b):
	#check range of loop number
	if num<41 or num>60:
		print "ERROR:Loop number is out of bound!"

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA3"

	if num>40 and num<50:
		n=num%10
		list1[1]="0xC"+str(n)

	if num>=50 and num<60:
		n=num%10
		list1[1]="0xD"+str(n)
	if num==60:
		list1[1]="0xE0"

	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	print output_bytes
	return output_bytes;

def timingLoopStart(num,time,mode,a,b):
	#check range of loop number
	if num<41 or num>60:
		print "ERROR:Loop number is out of bound!"

	##generate list 1*30
	list1=[0]*30

	#fill in variables
	list1[0]="0xA3"
	list1[1]="0x"+str(num)
	list1[2]=highValue(time)
	list1[3]=lowValue(time)
	list1[4]=mode
	list1[26]=highValue(a)
	list1[27]=lowValue(a)
	list1[28]=highValue(b)
	list1[29]=lowValue(b)

	##convert list to string
	string="".join(str(e) for e in list1)

	##convert string to bytes
	output_bytes=string.encode(encoding="utf-8")
	#print output_bytes
	return output_bytes;




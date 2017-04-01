

def highValue(a):
	high_time=(a>>8)&0xff
	return high_time;

def lowValue(a):
	low_time=a&0xff
	return low_time;

from tokenizer import *
from identifier import *

input='''


D=3-F

ADS = 30

'''


save=tokenizer(input)
print "save:",save

cleanR= cleanScanStringResult(save)
print "Tokens:", cleanR


T=identifier(cleanR)
print "Messages:",T




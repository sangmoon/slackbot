import time
import math
import random
from slacker import Slacker

'''
int getIndex(size, mon, day)
input
	size : phrase full size
	mon : current month
	day : current day
output
	generated integer index
'''
def getIndex(size, mon, day):
	section_size = math.ceil(size / 31.0)
	section_idx = mon % section_size
	#print section_size, section_idx

	if section_idx != 0 :
		index = (section_idx-1)*31 + (day-1)
	else :
		temp = (section_size-1)*31 + (day-1)
		if size > temp:
			index = temp
			#print "size > temp", index
		else:
			index = random.randrange(0,size) # random index
			#print "size <= temp", index
	return int(index)

token = 'TOKEN'
slack = Slacker(token)

now = time.localtime()

with open("./phrase.txt", "r") as f:
	lines = f.readlines()
	psize=len(lines) #phrase size
	select_idx = getIndex(psize, now.tm_mon, now.tm_mday)
	#print psize, select_idx
	message = lines[select_idx]

#send to slack bot
slack.chat.post_message('#hagsa', message, as_user=True)

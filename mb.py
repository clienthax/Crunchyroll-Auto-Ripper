import os
from collections import deque
queue = deque(open('videos.txt'))
while True:
	if len(queue) == 0:
		break
	video = queue.popleft()
	video = video.strip()#remove newline characters
	os.system('_start.bat '+video)
	if len(queue) == 1:
		print str(len(queue))+' video remaining'
	else:
		print str(len(queue))+' videos remaining'
'''
	file = open('videos.txt', 'w+')
	for url in queue:
		file.write(url)
	file.close()
'''
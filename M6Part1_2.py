import time
from threading import Thread
from datetime import datetime


thread_name=["name1","name2","name3","name4","name5",] #название потока

def get_thread(thread_name):
	time.sleep(1)
	print(f'имя потока {thread_name}\\n') 

t1=datetime.now()
threads=[Thread(target = get_thread, args=(i, )) for i in thread_name]

for t in threads:
	t.start()
for t in threads:
	t.join()
print("time paralel: ", (datetime.now()-t1).microseconds)

t1=datetime.now()
for i in thread_name:
	get_thread(i)

print("time line: ", (datetime.now()-t1).microseconds)

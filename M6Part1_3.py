import requests
from threading import Thread
import json
 

def get_html(link):
	r = requests.get(link)
	print()
	print(f"длина текста со страницы {link}:", len(r.text))
	

links=["https://ya.ru", "https://www.google.ru", "https://github.com/mojotman/lesson6", "https://www.youtube.com", "https://www.wikipedia.org"]

Threads = [Thread (target=get_html, args=(i, )) for i in links]

for t in Threads:
	t.start()
for t in Threads:
	t.join()

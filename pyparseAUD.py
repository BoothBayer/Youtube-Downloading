from pytube import YouTube
import time
import datetime
import os
from threading import Thread
x= 0
ytDlL = []
threads = []
def downloadYouTube(yt, path):
	try:
		if not os.path.exists(path):
			os.makedirs(path)
		print("Downloading " + yt.title)
		yt2 = yt.streams.filter(only_audio=True).first()
		yt2.download(output_path=path,filename_prefix="(AudioOnly)")
		print('Downloaded {} | {}'.format(yt.title, datetime.datetime.now()))
	except Exception as e:
		print("ERROR: ", e)

filepath = 'playlistLinks'
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		yt = YouTube(line.strip())
		ytDlL.append(yt)
		print("Added {} to ytDlL".format(yt))
		#downloadYouTube('{}'.format(line.strip()), './Directory', cnt)
		#print("Done Download")
		line = fp.readline()
		cnt += 1
for yt in ytDlL:
	process = Thread(target=downloadYouTube,args=[yt, './Directory'])
	print("Starting process {} | {}".format(x, yt.title))
	process.start()
	threads.append(process)
	x += 1
for process in threads:
	process.join()
print("quitting")
exit()

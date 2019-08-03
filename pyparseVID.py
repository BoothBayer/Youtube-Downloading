from pytube import YouTube
import time
import datetime
import sys
import os
from threading import Thread
threads = []
def percent(tem, total):
        x = float(total - tem)
        perc = (float(x) / float(total)) * float(100)
        return perc
a = 0 #used to stop percents from reposting
v = 0 #^
def progress_callback(stream,chunk,file_handle,bytes_remaining):
        global a
	global v
        size = stream.filesize
        y = round(percent(bytes_remaining,size),0)
	try:
		if int(y) != 0:
			if (100%(int(y)) == 0):
				if stream.includes_audio_track:
					if a != y:
						print('AUD: '+str(y)+'%')
						a = y
				elif stream.includes_video_track:
					if v != y:
						print('VID: '+str(y)+'%')
						v = y
	except Exception as e:
		print(e)
def downloadYouTube(videourl, path, cnt):
	try:
		yt = YouTube(videourl)
		yt.register_on_progress_callback(progress_callback)
		if not os.path.exists(path):
			os.makedirs(path)
		print(yt.title)
#		print(yt.streams.filter(adaptive=True).all()) #.order_by('resolution').desc().first()
		print("get 299vid")
		yt2 = yt.streams.get_by_itag('299') #itag299 is hd vid and 140 is matching audio
		processV = Thread(target=download, args=[yt2,path,'VID'])
		processV.start()
		threads.append(processV)
		print("get 140aud")
		yt2 = yt.streams.get_by_itag('140')
		processA = Thread(target=download, args=[yt2,path,'AUD'])
		processA.start()
		threads.append(processA)
		for process in threads:
			process.join()
		print('Downloaded {} | {}'.format(cnt, datetime.datetime.now()))
	except Exception as e:
		print("ERROR: ", e)
def download(stream,path,h):
	print('Downloading: ' + str(stream))
	try:
		if stream.includes_audio_track:
			print("includes audio", h)
		elif stream.includes_video_track:
			print("includes video", h)
		stream.download(output_path=path,filename_prefix=h)
	except Exception as e:
		print(stream," ERROR DL: ", e)
filepath = 'playlistLinks'
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		downloadYouTube('{}'.format(line.strip()), './Directory', cnt)
		print("Done Downloading")
		line = fp.readline()
		cnt += 1
print("quitting")
exit()

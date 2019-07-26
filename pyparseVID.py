from pytube import YouTube
import time
import datetime
from pytube import YouTube
import os

def comp_func(stream,file_handle):
	print("Downloaded: ", file_handle, " " ,stream)

def downloadYouTube(videourl, path, cnt):
	try:
		yt = YouTube(videourl)
		if not os.path.exists(path):
			os.makedirs(path)
		print("Downloading " + yt.title)
		yt2 = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first()
		yt2.download(output_path=path)
		print('Downloaded {} | {}'.format(cnt, datetime.datetime.now()))
	except Exception as e:
		print("ERROR: ", e)

filepath = 'playlistLinks'
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		print("Line {}: {}".format(cnt, line.strip()))
		downloadYouTube('{}'.format(line.strip()), './Directory', cnt)
		print("Done Download")
		line = fp.readline()
		cnt += 1
		print("Count increased")
print("quitting")
exit()

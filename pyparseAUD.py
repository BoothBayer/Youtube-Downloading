from pytube import YouTube
import time
import datetime
import os
import subprocess
import sys
def downloadYouTube(videourl, path, cnt):
	try:
		yt = YouTube(videourl)
		yt2 = yt.streams.filter(only_audio=True).first()
		if not os.path.exists(path):
			os.makedirs(path)
		print("Downloading " + yt.title)
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
		line = fp.readline()
		cnt += 1
print("quitting")
sys.exit()
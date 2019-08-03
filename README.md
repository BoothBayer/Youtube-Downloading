# Youtube-Downloading

Step 1: Create a text file with all the links for the videos you want to download.

Use the code below in powershell to get the list.

        $Playlist = ((Invoke-WebRequest "playlist-link").Links | Where {$_.class -match "playlist-video"}).href
        ForEach ($Video in $Playlist) {
        $s ="https://www.youtube.com" + $Video
        $s =$s.Substring(0, $s.IndexOf('&'))
            Write-Output ($s)
        }
        
Step 2: Once you have the list edit the code and change line 21 to give the filepath to your list of links.

Step 3: Change the download directory on line 27 to wherever you desire.

Step 4: Run the code.
NOTE:use ffmpeg tocombine vid and aud streams
ffmpeg -i video.mp4 -i audio.mp4 \
-c:v copy -c:a aac -strict experimental output.mp4

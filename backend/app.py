url = "https://x.com/i/status/1817224599467147384"
url2 = "https://x.com/i/status/1817240442540618158"
url3 = "https://x.com/cooltechtipz/status/1817148585508495577?t=DpvTc0zDjQgoRY2MS-7NNA&s=09"
url3y = "https://x.com/i/status/1817148585508495577"

tik = "https://www.tiktok.com/@mirajclips/video/7379931219456281898?is_from_webapp=1&sender_device=pc"
tik2 = "https://www.tiktok.com/@jkay_media/video/7375991228132838662?is_from_webapp=1&sender_device=pc"
insta = "https://www.instagram.com/reel/C9k6P8HuwqC/?utm_source=ig_web_copy_link"
insta2 = "https://www.instagram.com/reel/C9kZzKvN007/?utm_source=ig_web_copy_link"

face = "https://fb.watch/tC1BMUwdZS/"
you = "https://youtu.be/IQuf2Mj3AsQ?t=31"
you2 = "https://www.youtube.com/shorts/NEVwGEYNP0I?feature=share"

import logging
import yt_dlp
import os
import youtube_dl
import pafy



def download_twitter_video(url, output_path='videos/'):
    ydl_opts = {
        'outtmpl': f'{output_path}%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
         'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def download_youtube_video(url, output_path="videos/"):
    try:
        # Create a pafy object
        video = pafy.new(url)

        # Get the best video stream
        best_stream = video.getbest()

        # Download the video
        best_stream.download(filepath=f"{output_path}/{video.title}.{best_stream.extension}")
        print(f"Downloaded: {video.title}")

    except Exception as e:
        print(f"An error occurred: {e}")

        
def download_video(platform):
    urly = you
    # platform = "twitter"

    if platform.lower() == 'twitter':
        download_twitter_video(urly)
        print ({'status': 'success', 'message': 'Twitter video download started.'})
        
    elif platform.lower() == "youtube":
        download_youtube_video(urly)    
        print ({'status': 'success', 'message': 'YouTube Video video download started.'})
    
    else:
        print({'status': 'error', 'message': 'Unsupported platform.'})

if __name__ == '__main__':
    if not os.path.exists('videos'):
        os.makedirs('videos')
        
    download_video("Youtube")
    
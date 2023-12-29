import subprocess
import os

def run_ffmpeg(rtsp_url, rtmp_url):
    ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")
       
   ## ffmpeg_command = r"d:\ffmpeg-2023-12-04-git-8c117b75af-essentials_build\bin\ffmpeg.exe -rtsp_transport tcp -i {} -c:a aac -ar 44100 -ac 1 -c copy -f flv {}"

    ffmpeg_command = f'"{ffmpeg_path}" -rtsp_transport tcp -i {rtsp_url} -c:a aac -ar 44100 -ac 1 -c copy -f flv {rtmp_url}'
    subprocess.run(ffmpeg_command, shell=True)

def main():
    rtsp_url = input("Enter RTSP URL: ")
    rtmp_url = input("Enter RTMP URL: ")
    run_ffmpeg(rtsp_url, rtmp_url)

if __name__ == "__main__":
    main()

from flask import Flask, request, render_template_string
import subprocess
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        rtsp_url = request.form['rtsp_url']
        rtmp_url = request.form['rtmp_url']
        run_ffmpeg(rtsp_url, rtmp_url)
        return 'FFmpeg process started.'
    return '''
        <form method="post">
            RTSP URL: <input type="text" name="rtsp_url"><br>
            RTMP URL: <input type="text" name="rtmp_url"><br>
            <input type="submit" value="Run FFmpeg">
        </form>
    '''

def run_ffmpeg(rtsp_url, rtmp_url):
    ffmpeg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ffmpeg.exe")
    ffmpeg_command = f'"{ffmpeg_path}" -rtsp_transport tcp -i {rtsp_url} -c:a aac -ar 44100 -ac 1 -c copy -f flv {rtmp_url}'
    subprocess.run(ffmpeg_command, shell=True)

if __name__ == '__main__':
    app.run(debug=True)

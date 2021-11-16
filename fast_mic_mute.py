from flask import Flask, request
from subprocess import Popen
import socket

app = Flask(__name__)

print(f'''
*********
* Running: Now visit http://{socket.gethostbyname(socket.gethostname())}:8000 from your phone :) 
*********
''')

def exec_applescript(script):
    p = Popen(['osascript', '-e', script])

@app.route("/")
@app.route("/unmute")
def unmute():
    exec_applescript('set volume input volume 100')
    return make_html('mute', 'red')

@app.route("/mute")
def mute():
    exec_applescript('set volume input volume 0')
    return make_html('unmute', 'green')

def make_html(dest, color):
    return f'''
    <html>
        <head>
        <style>
        a {{
            background-color:{color};
            width:100%;
            margin-left:0;
            margin-right:0;
            padding-left:0;
            padding-right:0;
            display:block;
            text-align:center;
            height:100%;
            color:white;
            text-decoration: none;
            font-family: sans-serif;
        }}
        </style>
        <body style='margin:0px;'>
        <a href='/{dest}'>Click to {dest}</a>
        </body>
    </html>
    '''
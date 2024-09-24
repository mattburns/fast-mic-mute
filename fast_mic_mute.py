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
            width:100vw;
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            color:white;
            text-decoration: none;
            font-family: sans-serif;
            font-size: calc(5vw + 5vh);
        }}
        </style>
        </head>
        <body style='margin:0; padding:0;'>
        <a href='/{dest}'>Click to {dest}</a>
        </body>
    </html>
    '''
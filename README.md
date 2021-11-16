# fast-mic-mute
Use your phone as a big button to mute your laptop's mic. Works at the OS level so works for all video chat clients.

* Can't remember the shortcuts to (un)mute the mic in Zoom / Meet / Teams ?
* Fed up of scrambling to find the chat window when someone asks you a question?

[![demo video](https://i.imgur.com/dtn3doY.png)](https://youtu.be/HLCvgctujOY "How to use your phone to mute your mic in video calls")


## Install dependencies

    pip3 install flask
    pip3 install gunicorn

## Run the app on your laptop

    gunicorn fast_mic_mute:app  -b 0.0.0.0:8000

## Now toggle the mic from any browser on your network

Visit `http://[your-macbook-ip-address]:8000` from your phone. (It should tell you when you run the app)
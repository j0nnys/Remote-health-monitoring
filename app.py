from flask import Flask, render_template
import templogger
import time
import datetime
import tmp102

app = Flask(__name__)

@app.route('/')
def index():
    temp_c = str(round(tmp102.read_temp(), 2))
    entry = str(datetime.datetime.now())
    entry = entry + "," + temp_c + "\n"
    templateData = {
        'title':'IoT Application',
        'temp':temp_c
        }
    
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
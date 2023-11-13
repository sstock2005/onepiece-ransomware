from flask import Flask, send_file
from subprocess import check_output
import os


# GLOBALS #
app = Flask(__name__)
filename = r".\\dist\\king_of_the_pirates.exe"

# INDEX PAGE #
@app.route('/')
def home():
    return '<head><title>>:)</title></head><body><h1 style=\"text-align:center;\">すべての希望を捨てなさい。</h1></body>'

# DOWNLOAD FILE #
@app.route('/d')
def test():
    try:
        try:
            os.remove(filename)
        finally:
            check_output(r"pyinstaller --name king_of_the_pirates --uac-admin --console --hide-console hide-early --onefile main.py --clean --disable-windowed-traceback --i flag.ico --upx-dir C:\\UPX\\upx-4.2.0-win64")
            return send_file(filename, mimetype='application/octet-stream')
    except Exception as e:
        return str(e), 500

# APPLICATION RUN #
app.run('0.0.0.0', 8888, True)
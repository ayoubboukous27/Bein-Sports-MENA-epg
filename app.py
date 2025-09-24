from flask import Flask, send_file
import os

app = Flask(__name__)

EPG_FILE = "bein_sports_mena.xml"  # غيّر الاسم إذا مختلف

@app.route("/get-epg")
def get_epg():
    if os.path.exists(EPG_FILE):
        return send_file(EPG_FILE)
    else:
        return "EPG file not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

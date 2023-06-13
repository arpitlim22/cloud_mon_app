import psutil
from flask import flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_persent = psutil.cpu_percent()
    memory_persent = psutil.virtual_memory().percent
    Message = None
    if cpu_persent > 80 or memory_persent > 80:
        Message = "High cpu or memory detected"
    return f"CPU Utilisation: {cpu_persent} and Memory utilisation: {memory_persent}"

if __name__== '__main__':
    app.run(debug=True, host= '0.0.0.0')

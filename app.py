from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    username = os.getenv("USER") or os.getenv("USERNAME")
    
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    
    top_output = subprocess.check_output("top -bn1", shell=True).decode("utf-8")

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> Methilesh</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

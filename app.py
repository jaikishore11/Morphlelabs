from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop_info():
    
    name = "Jaikishore"  
    username = subprocess.getoutput("whoami")  # Get the system username
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')  # IST time
    htop_output = subprocess.getoutput("htop -b -n 1")  # Execute htop command

    # Return information
    return f"""
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {ist_time}

    HTOP Output:
    {htop_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

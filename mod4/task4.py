from flask import Flask
import sys
import shlex
import subprocess

app = Flask(__name__)

# uptime -p | python3 mod4/task4.py
# UPTIME = sys.stdin.read()


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    command_str = f"uptime"
    result = subprocess.run([command_str, '-p'], capture_output=True).stdout.decode('utf8')
    return f"Current uptime is {result}"


if __name__ == '__main__':
    app.run(debug=True)










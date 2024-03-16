from flask import Flask
import sys

app = Flask(__name__)

# uptime -p | python3 mod4/task4.py
UPTIME = sys.stdin.read()


@app.route("/uptime", methods=['GET'])
def uptime() -> str:
    return f"Current uptime is {UPTIME}"


if __name__ == '__main__':
    app.run(debug=True)





#ps?arg=a&arg=u&arg=x
import shlex, subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/ps", methods=["GET"])
def ps() -> str:
    args: list[str] = request.args.getlist('arg')
    user_cmd = ''.join(args)
    clean_user_cmd = shlex.quote(user_cmd)
    result = subprocess.run(['ps', clean_user_cmd], capture_output=True).stdout.decode('utf8')
    # result = subprocess.check_output(['ps', clean_user_cmd]).decode('utf-8')
    return f'<pre>Your result</pre>\n{result}'


if __name__ == "__main__":
    app.run(debug=True)
import subprocess
import shlex
import os
import signal
from flask import Flask


app = Flask(__name__)


def terminate_processes(pid_list: list):
    res = [os.kill(int(pid), signal.SIGKILL) for pid in pid_list]


def main(port: int):
    cmd = f'lsof -i :{port}'
    args = shlex.split(cmd)
    res = subprocess.run(args, capture_output=True)
    lsof_output = res.stdout.decode('utf8')
    pid_list = []
    for line in lsof_output.split('\n')[1:-1]:
        pid = line.split()[1]
        pid_list.append(pid)
    if pid_list:
        terminate_processes(pid_list)
    app.run(port=port)


if __name__ == '__main__':
    port = int(input())
    main(port)
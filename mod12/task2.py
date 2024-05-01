import subprocess


def process_count(username: str) -> int:
    # количество процессов, запущенных из-под
    # текущего пользователя username
    cmd = f"ps -u {username} -o pid= | wc -l"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        return int(output.strip())
    return -1


def total_memory_usage(root_pid: int) -> float:
    # суммарное потребление памяти древа процессов
    # с корнем root_pid в процентах
    cmd = f"ps --ppid {root_pid} -o rss= | awk '{{sum+=$1}} END {{print sum}}'"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        total_memory = int(output.strip())
        return total_memory / (1024 ** 2)
    return -1
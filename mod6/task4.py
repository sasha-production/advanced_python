import logging
import json
from itertools import groupby
import subprocess
import shlex

def get_critical_logs():
    command = '''grep -cE '"time": "05:[01].*?"level": "CRITICAL"' skillbox_json_messages.log'''
    cmd = shlex.split(command)
    critical_logs = subprocess.run(cmd, capture_output=True).stdout.decode('utf8')
    return critical_logs.strip()


def get_count_logs_with_dog():
    command ="grep -c 'message.*dog' skillbox_json_messages.log"
    cmd = shlex.split(command)
    logs_with_dog_count = subprocess.run(cmd, capture_output=True).stdout.decode('utf8')
    return logs_with_dog_count.strip()
def main():
    message_type_per_day = {}
    with open('skillbox_json_messages.log', encoding='utf-8') as file:
        data = [json.loads(line) for line in file.readlines()]
        for log in data:
            message_type_per_day[log['level']] = message_type_per_day.get(log['level'], 0) + 1

        hour_max_logs = max([(key, [*value]) for key, value in groupby(data, key=lambda item: item['time'][:2])], key=lambda item: len(item[1]))[0]
        critical_logs = get_critical_logs()
        logs_with_dog = get_count_logs_with_dog()
        words_dict = {}
        for log in data:
            if log['level'] == 'WARNING':
                words = log['message'].split()
                for word in words:
                    words_dict[word] = words_dict.get(word, 0) + 1
        most_popular_word = max(words_dict.items(), key=lambda item: item[1])
        print(message_type_per_day, hour_max_logs, critical_logs, logs_with_dog, most_popular_word, sep='\n')


if __name__ == '__main__':
    main()